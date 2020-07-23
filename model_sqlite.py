import sqlite3

# ---------------------------------------------------------

def createTables():
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    #c.execute("DROP TABLE code")
    #c.execute("DROP TABLE edition")

    c.execute('''
        CREATE TABLE IF NOT EXISTS code (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT DEFAULT 'Insert your code here ...',
            language VARCHAR(50) DEFAULT 'py',
            createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updatedAt TIMESTAMP
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS edition (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip INT,
            user_agent VARCHAR(255),
            TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# ---------------------------------------------------------

def createCode():
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO code
    ''')

    uid = c.lastrowid

    conn.commit()
    conn.close()

    return uid

# ---------------------------------------------------------

def getCode(id):
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    result = c.execute('''
        SELECT
            code,
            language
        FROM code
        WHERE id = ?
    ''', (id))

    conn.commit()
    conn.close()

    return result

# ---------------------------------------------------------

def getAllCode():
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    result = c.execute('''
        SELECT
            code,
            language
        FROM code
        ORDER BY
            updatedAt DESC,
            createdAt DESC
    ''')

    conn.commit()
    conn.close()

    return result

# ---------------------------------------------------------

def updateCode(id, code, language):
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    result = c.execute('''
        UPDATE TABLE code
        (code, language, updatedAt)
        SET(?,?, NOW())
        WHERE id = ?
    ''', (code, language, id))

    conn.commit()
    conn.close()

    return result

# ---------------------------------------------------------

def createEdition(ip, user_agent):
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO edition
        VALUES(?,?)
    ''', (ip, user_agent))

    uid = c.lastrowid

    conn.commit()
    conn.close()

    return uid

# ---------------------------------------------------------

def getEdition():
    conn = sqlite3.connect('shareCode.db')
    c = conn.cursor()

    result = c.execute('''
        SELECT ip, user_agent, date
        FROM edition
        ORDER BY date DESC
    ''')

    conn.commit()
    conn.close()

    return result