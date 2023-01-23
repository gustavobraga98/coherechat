import cohere

def ask_key():
    COHEREAPI = str(input("Insert you cohere API> "))
    try:
        co = cohere.Client(COHEREAPI)
        rcv = co.chat("")
        return(True,co,rcv.session_id)
    except:
        return(False,0,0)