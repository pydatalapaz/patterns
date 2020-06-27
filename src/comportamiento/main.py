from chain import Request, MidddlewareHandler, ControllerHandler
from observer import ObserverOne, ObserverTwo, Subject
from command import Application
from strategy import ApiDemo, JsonParser, XMLParser


ctrl = ControllerHandler()
ctrl.set_anterior(MidddlewareHandler())
ctrl.handle_request(Request())

subject = Subject()
subject.add_observer(ObserverTwo())
subject.add_observer(ObserverOne())
subject.state = 'Changed'
subject.state = 'Changed 2'
subject.state = 'Changed 3'

app = Application()
app.add_btn_click()
app.add_btn_click()
app.add_btn_click()
app.add_btn_click()
app.delete_btn_click()
app.undo()
app.undo()


api_json = ApiDemo(JsonParser())
api_xml = ApiDemo(XMLParser())
api = ApiDemo()

api_json.send('a')
api_xml.send('a')
api.send('a')