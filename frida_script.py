import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
if (ObjC.available)
{
    for (var className in ObjC.classes)
    {
        if (ObjC.classes.hasOwnProperty(className))
        {
            console.log(className);
        }
    }
}
else
{
    console.log("Objective-C Runtime is not available!");
}
"""

process = frida.attach("target_app")
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running Frida script...')
script.load()
sys.stdin.read()