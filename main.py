
import psycopg2

conn = psycopg2.connect(
    dbname="practice",
    user="postgres",
    password="am1rov_008",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


def transfer_money(sender_account_number, receiver_account_number, amount):
    try:
        cur.execute("BEGIN")
        cur.execute("""SELECT balance FROM bank_accounts WHERE account_number = %s""", (sender_account_number,))
        sender_balance = cur.fetchone()[0]

        if sender_balance < amount:
            print("Balansingizda mablag' yetarli emas!.")
            return

        cur.execute("""SELECT COUNT(*) FROM bank_accounts WHERE account_number = %s""", (receiver_account_number,))
        receiver_exists = cur.fetchone()[0]
        if receiver_exists == 0:
            print("Receiver account does not exist. Transaction failed.")
            return
        cur.execute("""UPDATE bank_accounts SET balance = balance - %s WHERE account_number = %s""", (amount, sender_account_number))
        cur.execute("""UPDATE bank_accounts SET balance = balance + %s WHERE account_number = %s""", (amount, receiver_account_number))

        cur.execute("COMMIT")
        print("Transaction successful.")

    except Exception :
        cur.execute("ROLLBACK")
        print("Transaction muvaffaqiyatsizlikka uchradi. Xatolik:", str(Exception))



# Example usage
transfer_money(4642,3308, 6083)