contract_headers = [
    'ID',
    'CONTRACT_NAME',
    'DEPOSIT',
    'END_DATE',
    'LINK_ID',
    'START_DATE',
    'TS_TIMESTAMP',
    'FI_ACCOUNT_ID',
    'PD_CONTACT_PERSON_ID',
    'CO_STATE_ID',
    'CO_TYPE_ID',
    'CO_PAYMENT_SCHEDULE_TYPE_ID',
    'PD_SALES_PERSON_ID',
    'IS_EXCLUDE_FROM_UNFLOWN_HOURS',
    'IS_SHOWN_IN_PAYMENT_REQUEST',
    'INCLUDE_DOMESTIC_RATE',
    'ENABLE_MANAGEMENT_FEE',
    'MINIMUM_REQUIRED_BALANCE',
    'PAYMENT_TERMS',
    'CONTRACT_MS_ID',
    'PAYMENT_SCHEDULE_MS_ID',
    'SYMBOL',
]

payment_schedule_headers = [
    'LINK_ID',                      # contract link id
    'CONTRACT_MS_ID',               # contract aggregate id
    'DEPOSIT',                      # deposit amount cents
    'PAYMENT_SCHEDULE_MS_ID',       # ps aggr_id
    'CO_PAYMENT_SCHEDULE_TYPE_ID',  # ps type id
    'NAME',                         # ps type name
    'ID',
    'AMOUNT_IN_CENTS',              # ps line amount
    'DUE_DATE',                     # ps line due date
    'CO_CONTRACT_ID',
    'LINK_ID_1',
    'PAYMENT_SCHEDULE_LINE_MS_ID',  # ps line aggr_id
]

management_fee_headers = [
    'LINK_ID',
    'CONTRACT_MS_ID',
    'VJ_AIRCRAFT_TYPE_ID',
    'ID',
    'TOTAL_AMOUNT_CENTS',
    'USED_AMOUNT_CENTS',
    'VALID_FROM',
    'VALID_TO',
    'DUE_DATE',
    'NOTES',
    'FEE_RATE',
    'CO_DETAIL_ID',
    'FI_INVOICE_ID',
    'FI_LINK_ID_1',
    'MANAGEMENT_FEE_LINE_MS_ID',
    'DESCRIPTION',
    'MANAGEMENT_FEE_MS_ID',
    'MANAGEMENT_FEE_SCHEDULE_TYPE',
    'NAME',
]

co_details_headers = [
    'XID',
    'CONTRACT_LINK_ID',
    'CONTRACT_ID',
    'CONTRACT_DETAIL_ID',
    'ACTYPE_ID',
    'ACTYPE_NAME',
    'MANAGEMENT_FEE_COUNT',
]

MOCKED_VALUE = {
  "correlationId": "111-11",
  "aggregateId": "1fc47cbd-539e-42f9-804e-d613800216a9",
  "accountCurrency": "$",
  "accountId": 51575,
  "paymentSchedule": {
    "aggregateId": "99376434-0e1a-4615-b88b-20733a140031",
    "contractAggregateId": "1fc47cbd-539e-42f9-804e-d613800216a9",
    "paymentOptionsDescription": "Annual",
    "installmentsQuantity": 1,
    # "advanceNoticeDays": 30,
    "deposit": {
      "aggregateId": "154c457f-a864-498c-8ee3-3f6202f2c46c",
      "contractAggregateId": "1fc47cbd-539e-42f9-804e-d613800216a9",
      # "description": "Program Security Deposit - Challenger 350",
      "amountInCents": 12,
      "dueDate": "2016-05-31",
      # "invoiceId": None,
      # "invoiceLinkId": None,
      # "invoiceStatus": None
    },
    "paymentScheduleLines": [
      {
        "aggregateId": "34b1571b-7f3e-4b2f-a9c5-caedd865ce3d",
        "paymentScheduleAggregateId": "99376434-0e1a-4615-b88b-20733a140031",
        # "invoiceId": None,
        # "invoiceLinkId": None,
        "dueDate": "2016-05-31",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 77711,
        # "invoiceStatus": None,
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      },
      {
        "aggregateId": "794b0a99-3222-41d2-b1ae-96f05e2740cf",
        "paymentScheduleAggregateId": "99376434-0e1a-4615-b88b-20733a140031",
        # "invoiceId": None,
        # "invoiceLinkId": None,
        "dueDate": "2017-05-31",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 0,
        # "invoiceStatus": None,
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      },
      {
        "aggregateId": "c2fe496a-c959-4f7c-8059-d23dd288f045",
        "paymentScheduleAggregateId": "99376434-0e1a-4615-b88b-20733a140031",
        # "invoiceId": None,
        # "invoiceLinkId": None,
        "dueDate": "2018-05-31",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 44587500,
        # "invoiceStatus": None,
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      }
    ]
  },
  "managementFees": [],
  "revision": {
    "id": None,
    "revisionNumber": 1,
    "username": "GLOBALVIEW.CR",
    "fullName": "GLOBALVIEW.CR",
    "activityTypeId": 8,
    "postDate": "2019-07-03T13:12:59.202934",
    "note": "Contracts data synchronization with Globalview testing state script15"
  }
}

ANOTHER_VALUE = {
  "correlationId": "37447567",
  "aggregateId": "252f69ba-e167-4364-ba1c-10e4277f3c02",
  "accountCurrency": "$",
  "accountId": 62227,
  "paymentSchedule": {
    "aggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
    "contractAggregateId": "252f69ba-e167-4364-ba1c-10e4277f3c02",
    "paymentOptionsDescription": "Bi-Monthly",
    "installmentsQuantity": 6,
    # "advanceNoticeDays": 30,
    "deposit": {
      "aggregateId": "d6f87e01-69de-461a-97ee-44b877ef3b63",
      "contractAggregateId": "252f69ba-e167-4364-ba1c-10e4277f3c02",
      # "description": "Program Security Deposit - Challenger 350",
      "amountInCents": 0,
      "dueDate": "2018-06-29",
      # "invoiceId": "t_249045",
      # "invoiceLinkId": 172232,
      # "invoiceStatus": {
      #   "statusId": 8,
      #   "statusDescription": "Raised",
      # },
    },
    "paymentScheduleLines": [
      {
        # "aggregateId": "f17ea734-3769-4f3c-a04f-6128799086b2",
        # "paymentScheduleAggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
        "aggregateId": None,
        "paymentScheduleAggregateId": None,
        # "invoiceId": "t_249046",
        # "invoiceLinkId": 172233,
        "dueDate": "2018-06-29",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 9296250,
        # "invoiceStatus": {
          # "statusId": 8,
          # "statusDescription": "Raised"
        # },
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      },
      {
        # "aggregateId": "fd2b2835-debe-47af-9fbf-4bfca2178baa",
        # "paymentScheduleAggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
        "aggregateId": None,
        "paymentScheduleAggregateId": None,
        # "invoiceId": "t_249048",
        # "invoiceLinkId": 172235,
        "dueDate": "2018-09-29",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 9296250,
        # "invoiceStatus": {
          # "statusId": 8,
          # "statusDescription": "Raised"
        # },
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      },
      {
        # "aggregateId": "56f9af8e-2d91-4640-8bf8-01f84c1ac415",
        # "paymentScheduleAggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
        "aggregateId": None,
        "paymentScheduleAggregateId": None,
        # "invoiceId": "t_249047",
        # "invoiceLinkId": 172234,
        "dueDate": "2018-12-14",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 12395000,
        # "invoiceStatus": {
          # "statusId": 8,
          # "statusDescription": "Raised"
        # },
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      },
      {
        # "aggregateId": "78a12ebd-4911-404f-849d-12b20bd2e25c",
        # "paymentScheduleAggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
        "aggregateId": None,
        "paymentScheduleAggregateId": None,
        # "invoiceId": "t_248527",
        # "invoiceLinkId": 171812,
        "dueDate": "2019-07-01",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 15493800,
        # "invoiceStatus": {
          # "statusId": 8,
          # "statusDescription": "Raised"
        # },
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      },
      {
        # "aggregateId": "7ae95582-720b-4588-a0c6-49af4ef76d1b",
        # "paymentScheduleAggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
        "aggregateId": None,
        "paymentScheduleAggregateId": None,
        # "invoiceId": None,
        # "invoiceLinkId": None,
        "dueDate": "2019-07-05",
        "description": "123",
        # "amountInCents": 123,
        # "invoiceStatus": None,
        # "isPaid": False,
        # "isAdHoc": True,
        # "isActive": True
      },
      {
        "aggregateId": None,
        "paymentScheduleAggregateId": None,
        #"aggregateId": "22e06f86-4be6-4382-b5c2-7e44d4997516",
        #"paymentScheduleAggregateId": "2f8d8f4f-fdc0-45d7-807f-c5ada6f8bdd5",
        # "invoiceId": "t_249054",
        # "invoiceLinkId": 172241,
        "dueDate": "2021-05-04",
        "description": "Imported from GlobalView (edit me)",
        # "amountInCents": 0,
        # "invoiceStatus": {
          # "statusId": 8,
          # "statusDescription": "Raised"
        # },
        # "isPaid": False,
        # "isAdHoc": False,
        # "isActive": True
      }
    ]
  },
  "managementFees": [
    {
      #"aggregateId": "d99339db-a4a2-42da-8e91-d58cd7751b09",
      "aggregateId": "",
      #"contractAggregateId": "252f69ba-e167-4364-ba1c-10e4277f3c02",
      "contractAggregateId": "",
      "managementFeeOptionsId": 2,
      "managementFeeOptionsDescription": "Single Payment",
      "acTypeId": 10,
      "managementFeePayments": [
        {
          #"aggregateId": "a13cc4fa-52c2-4689-b674-b091037524c2",
          "aggregateId": "",
          #"managementFeeAggregateId": "d99339db-a4a2-42da-8e91-d58cd7751b09",
          "managementFeeAggregateId": "",
          "dateFrom": "2019-06-06",
          "dateTo": "2019-06-06",
          "dueDate": "2019-06-06",
          "description": "toketas",
          "amountInCents": 666,
          "amountUsedInCents": 0,
          "balanceInCents": 2200,
          "managementFeeRateCents": 15840,
          "invoiceId": "t_248362",
          "invoiceLinkId": 171698,
        },
      ]
    }
  ],
  "revision": {
    "id": None,
    #"revisionNumber": 1,
    "username": "GLOBALVIEW.CR",
    "fullName": "GLOBALVIEW.CR",
    "activityTypeId": 8,
    "postDate": "2019-07-05T19:30:23.182798",
    "note": "Contracts data synchronization with Globalview tesst"
  }
}

ANOTHER_KEY = { "aggregateId": "252f69ba-e167-4364-ba1c-10e4277f3c02" }

MOCKED_KEY = { "aggregateId": "1fc47cbd-539e-42f9-804e-d613800216a9" }
