import aiocoap.resource as resource
import aiocoap
from model.capsule_presence_sensor import CapsulePresenceSensorDescriptor
class CapsulePresenceSensorResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.capsule_presence_sensor = CapsulePresenceSensorDescriptor()

    async def render_get(self, request):
        print("CapsulePresenceSensorResource -> GET Request Received ... ")
        print("CapsulePresenceSensorResource -> Reading updated capsule presence value ... ")
        self.capsule_presence_sensor.measure_capsule_presence()
        print("CapsulePresenceSensorResource -> Updated Capsule Presence Value : %s" % self.capsule_presence_sensor.value)

        payload_string = self.capsule_presence_sensor.to_json()
        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))