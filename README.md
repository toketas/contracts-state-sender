## Setting up
1. After installing the python dependencies (located on requirements.txt), you
   must export 3 tables from GV. Steps to export below.

2. To run this script the following files are needed in the same folder:
   *header.dsv*, *payments.dsv*, *management_fees.dsv*

### Exporting tables

1. For each query, do the following on *sqldeveloper*:

    - Execute the query
    - Right click on the result table
    - Select option 'Export...'
    - In the wizard, change the format to: *delimited*
    - Change the delimiter value to: @
    - Save the file according to the Query (header.dsv, payment.dsv or
      management_fees.dsv)

2. Queries:

   Query contracts without ms_id - header.dsv

   SELECT co.*, cur.SYMBOL FROM CO_CONTRACTS co
   INNER JOIN FI_ACCOUNTS acc ON acc.ID = co.FI_ACCOUNT_ID
   JOIN VJ_CURRENCIES cur ON cur.ID = acc.VJ_CURRENCY_ID
   WHERE CO_STATE_ID != 5
   AND co.ID IN (select MAX(ID) FROM CO_CONTRACTS group by link_id)
   AND CONTRACT_MS_ID IS NULL
   ORDER BY link_id;
   ------------------------------------

   Query payment schedule lines - payments.dsv

   SELECT co.LINK_ID, co.CONTRACT_MS_ID, co.DEPOSIT,
       co.PAYMENT_SCHEDULE_MS_ID, co.CO_PAYMENT_SCHEDULE_TYPE_ID,
       pst.NAME, ps.*
   FROM CO_CONTRACTS co
   INNER JOIN CO_DUE_PAYMENTS ps ON ps.CO_CONTRACT_ID = co.ID
   LEFT JOIN CO_PAYMENT_SCHEDULE_TYPES pst ON pst.ID = co.CO_PAYMENT_SCHEDULE_TYPE_ID
   WHERE co.LINK_ID IN (
       SELECT LINK_ID FROM CO_CONTRACTS
       WHERE CO_STATE_ID != 5
       AND ID IN (SELECT MAX(ID) FROM CO_CONTRACTS GROUP BY link_id)
       AND CONTRACT_MS_ID IS NULL)
   AND co.id IN (SELECT MAX(id) FROM co_contracts GROUP BY link_id);
   -----------------------------------

   Query management fee lines - management_fees.dsv

   SELECT * FROM co_contracts co
   JOIN co_details cd ON cd.co_contract_id = co.id
   JOIN co_detail_management_fee mf ON mf.co_detail_id = cd.id
   AND co.id IN (SELECT MAX(id) FROM co_contracts GROUP BY link_id)
   WHERE co.link_id IN (
       SELECT link_id FROM CO_CONTRACTS
       WHERE CO_STATE_ID != 5
       AND ID IN (SELECT MAX(ID) FROM CO_CONTRACTS GROUP BY link_id)
       AND CONTRACT_MS_ID IS NULL
   );
   ----------------------------------


## Testing
1. Before running this script, you must test it first since any schema update
(contracts-state or GV table) can break this script.

2. Command to test:

    python3 tester-contracts.py

## Running

