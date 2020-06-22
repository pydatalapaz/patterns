class DBConn:
    def __init__(self):
        pass

def main():
    conn = DBConn()
    conn2 = DBConn()
    conn3 = conn

    conn.demo = 1

    if conn == conn2:
        print("S")
    else:
        print("N")

    print(conn3.demo)

if __name__ == "__main__":
    main()

    
    
    
