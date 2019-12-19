#!/bin/python3
# -*- coding: utf-8 -*-


# For more info, check API:
#   https://docs.confluent.io/current/clients/confluent-kafka-python/index.html
# Configuration:
#   https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md

import json
import csv
import os

from datetime import datetime
from utils import (contract_headers, payment_schedule_headers,
                   management_fee_headers)

delimiter = '@'
backend_url = 'http://localhost:8080/v1/aircraft'

conf = {
    'schema.registry.url': 'http://172.16.0.50:30003',
    'default.topic.config': {'acks': 'all'},
    'bootstrap.servers': 'tcp.k8s.monitoratec.local:30000'
}

def to_date(date_str):
    return  datetime.strptime(date_str.split(' ')[0], "%d/%m/%y").strftime('%Y-%m-%d')

def build_payment_schedule_line(row):
    payment_line = {}
    payment_line['aggregateId'] = row['PAYMENT_SCHEDULE_LINE_MS_ID'] if row['PAYMENT_SCHEDULE_LINE_MS_ID'] else None
    payment_line['paymentScheduleAggregateId'] = row['PAYMENT_SCHEDULE_MS_ID'] if row['PAYMENT_SCHEDULE_MS_ID'] else None
    payment_line['dueDate'] =  to_date(row['DUE_DATE'])
    #payment_line['description'] = row['DESCRIPTION'] # TODO check
    payment_line['amountInCents'] = row['AMOUNT_IN_CENTS']
    return payment_line

def build_contract(row):
    contract = {}
    contract['accountCurrency'] = row['SYMBOL']
    contract['correlationId'] = row['ID']
    contract['paymentSchedule'] = {}
    contract['managementFees'] = {}
    contract['revision'] = None
    contract['id'] = row['ID']
    contract['aggregateId'] = row['CONTRACT_MS_ID'] if row['CONTRACT_MS_ID'] else None
    contract['accountId'] = int(row['FI_ACCOUNT_ID'])
    return contract

def build_management_fee(row):
    return {
        'aggregateId': row['MANAGEMENT_FEE_MS_ID'],
        'contractAggregateId': row['CONTRACT_MS_ID'],
        'managementFeeOptionsId': row['MANAGEMENT_FEE_SCHEDULE_TYPE'],
        'managementFeeOptionsDescription': row['DESCRIPTION'],
        'acTypeId': row['VJ_AIRCRAFT_TYPE_ID'],
        'managementFeePayments': [],
    }

def build_management_fee_payment(row):
    return {
        'aggregateId': row['MANAGEMENT_FEE_LINE_MS_ID'] if row['MANAGEMENT_FEE_LINE_MS_ID'] else None,
        'managementFeeAggregateId': row['MANAGEMENT_FEE_MS_ID'] if row['MANAGEMENT_FEE_MS_ID'] else None,
        'linkId': None, # TODO: double-check
        'description': row['DESCRIPTION'],
        'dateFrom': to_date(row['VALID_FROM']),
        'dateTo': to_date(row['VALID_TO']),
        'dueDate': to_date(row['DUE_DATE']),
        'amountInCents': int(row['TOTAL_AMOUNT_CENTS']),
        'amountUsedInCents': int(row['USED_AMOUNT_CENTS']),
        # 'balanceInCents': 0, # TODO double check
        'managementFeeRateCents': row['FEE_RATE'],
        'invoiceId': row['FI_INVOICE_ID'],
        'invoiceLinkId': row['FI_LINK_ID_1'],
    }

def import_contracts():
    with open('header.dsv') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
        contracts = {}
        for i, row in enumerate(reader):
            # Header
            if row[0] == "ID":
                continue

            row_formatted = {}
            for i, value in enumerate(row):
                row_formatted[contract_headers[i]] = value
            contracts[row_formatted['LINK_ID']] = build_contract(row_formatted)
        print('============================')
        print('Finished processing header')

    with open('payments.dsv') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
        for i, row in enumerate(reader):
            # Header
            if row[0] == "LINK_ID":
                continue

            row_formatted = {}
            for i, value in enumerate(row):
                row_formatted[payment_schedule_headers[i]] = value
            contract = contracts.get(row_formatted['LINK_ID'])
            if not contract:
                print('couldnt find contract of link_id: {} - {}'.format(row_formatted['LINK_ID'], row_formatted))
                assert False
                continue

            payment_schedule = contract['paymentSchedule']
            payment_schedule_line = build_payment_schedule_line(row_formatted)
            if payment_schedule:
                payment_schedule['paymentScheduleLines'].append(payment_schedule_line)
            else:
                contract['paymentSchedule'] = {
                    'aggregateId': row_formatted['PAYMENT_SCHEDULE_MS_ID'] if
                                    row_formatted['PAYMENT_SCHEDULE_MS_ID'] else None,
                    'contractAggregateId': row_formatted['CONTRACT_MS_ID'] if row_formatted['CONTRACT_MS_ID'] else None,
                    'paymentOptionsDescription': row_formatted['NAME'],
                    'installmentsQuantity': 1,
                    'paymentScheduleLines': [payment_schedule_line],

                }
        print('============================')
        print('Finished processing payments')

    with open('management_fees.dsv') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
        for i, row in enumerate(reader):
            # Header
            if row[0] == "LINK_ID":
                continue

            row_formatted = {}
            for i, value in enumerate(row):
                row_formatted[management_fee_headers[i]] = value

            contract = contracts.get(row_formatted['LINK_ID'])
            if not contract:
                print('couldnt find contract of link_id: {}'.format(row_formatted['LINK_ID']))
                continue

            management_fees = contract['managementFees']

            management_fee_payment = build_management_fee_payment(row_formatted)
            if management_fees:
                # check managementFee
                management_fee = management_fees.get(row_formatted['VJ_AIRCRAFT_TYPE_ID'])
                if management_fee:
                    management_fee['managementFeePayments'].append(management_fee_payment)
                else:
                    management_fees[row_formatted['VJ_AIRCRAFT_TYPE_ID']] = build_management_fee(row_formatted)
                    management_fees[row_formatted['VJ_AIRCRAFT_TYPE_ID']]['managementFeePayments'] = [management_fee_payment]
            else:
                management_fees = {}
                management_fees[row_formatted['VJ_AIRCRAFT_TYPE_ID']] = build_management_fee(row_formatted)
                management_fees[row_formatted['VJ_AIRCRAFT_TYPE_ID']]['managementFeePayments'] = [management_fee_payment]
                contract['managementFees'] = management_fees

        print('============================')
        print('Finished processing management fees')
    return contracts

def build_payload(contracts):
    result = []
    for key in contracts.keys():
        contract = contracts[key]
        management_fee = []
        if contract['managementFees']:
            for mfee_key in contract['managementFees'].keys():
                management_fee.append(contract['managementFees'][mfee_key])
        contract['managementFees'] = management_fee
        contract['revision'] = {
          "id": None,
          # "revisionNumber": 1,
          "username": "GLOBALVIEW.CR",
          "fullName": "GLOBALVIEW.CR",
          "activityTypeId": 8,
          "postDate": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
          "note": "Updating contract via script"
        }
        result.append(contract)
    return result

contracts = import_contracts()

payloads = build_payload(contracts)
for contract in payloads:
    print(json.dumps(contract, indent=4, sort_keys=False))
    input('[ENTER] to print next contract =============')
    os.system('cls' if os.name == 'nt' else 'clear')
