from .iq import IqProtocolEntity
from yowsup.structs import ProtocolTreeNode
class BroadcastListIqProtocolEntity(IqProtocolEntity):
    """
    <iq id="1413891207-1" xmlns="w:b" type="get" to="s.whatsapp.net">
        <lists></lists>
    </iq>
    """
    def __init__(self):
        super(BroadcastListIqProtocolEntity, self).__init__("w:b", _type="get")

    def toProtocolTreeNode(self):
        node = super(BroadcastListIqProtocolEntity, self).toProtocolTreeNode()
        node.addChild(ProtocolTreeNode('lists'))
        return node
