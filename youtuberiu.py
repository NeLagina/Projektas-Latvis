import multiprocessing
import asyncio
import socketio

from functools import partial




#NELAGINOS MODULEI :D
from modules import handler
from modules import tts
#
#TOKENAS WEBSOCKET
#https://streamlabs.com/dashboard#/settings/api-settings
# API TOKEN > SOCKET API
Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6IjMxMkM0NDAwMTk2RUU1NTY0MjE4RUFEODY1N0I3QzFGNDZENUU1MTFDNTk2MjlFQjlEMDI5NDhDRDI5ODFGQjI2QTgxM0QyMzE1RjBFNUUxMjRBM0M3MkI3RUI4QzdFRDQ4ODMxNjlGNDFGMkVGQzg4M0Y4RUY4RDBDNzQxQTZBMDEzQkMzMUZGRDFDNTQ5RkVERUFGNzhEREE1NzQ5QTkzREVCNUJDQTFGOTJBMEU5Nzk3QzQ1M0RCNkE4QTIxRkQ5NEE0NDYyOTI0RjZGRENBNjFCMjM5NjQ2NTE4MUY4QTg3QzlGQ0U2MTQxMjYxRUEzNzQ5ODA0RDAiLCJyZWFkX29ubHkiOnRydWUsInByZXZlbnRfbWFzdGVyIjp0cnVlLCJ5b3V0dWJlX2lkIjoiVUMyUmc1a2V3cFMwUlR6blE2MUMwQ2pRIn0.8X18HzCs91pD_uZWxI39HhEb3NqFbRwccqOX9gVD7MI"
#



#logger=True, engineio_logger=True
sio = socketio.AsyncClient()
@sio.event
async def connect():
    print('Prijunkta Prie StreamLabs Serverio')

@sio.event
async def disconnect():
    print('Atsijunget Nuo StreamLabs Serverio')



@sio.on('event')
async def handle_event(eventData):
    if eventData['type'] == "donation" or "superchat" or "subscription" or "follow":
        process_target = partial(handler.don, eventData)
        
        # Create a new process and start it
        process = multiprocessing.Process(target=process_target)
        process.start()
    else:
        print("GAUTA zinute")
        print(eventData)




async def main():
    await sio.connect('https://sockets.streamlabs.com?token=' + Token)
    await sio.wait()
if __name__ == '__main__':
    tts.text_to_speech("Latvis Jungesi")
    asyncio.run(main())
        

