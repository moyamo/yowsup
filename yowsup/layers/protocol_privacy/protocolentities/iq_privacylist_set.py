from yowsup.layers.protocol_iq.protocolentities import IqProtocolEntity
from yowsup.structs import ProtocolTreeNode

class SetPrivacyListIqProtocolEntity(IqProtocolEntity):
    """
    <iq id="{{{id}}}" xmlns="jabber:iq:privacy" type="set">
     <query>
      <list name="default">
       <item type="jid" value="{{{jid}}}" action="deny" order="1" />
       <item type="jid" value="{{{jid}}}" action="deny" order="2" />
       <item type="jid" value="{{{jid}}}" action="deny" order="3" />
      </list>
     </query>
    </iq>
    """
    def __init__(self, blockedJids):
        super(SetPrivacyListIqProtocolEntity, self).__init__("jabber:iq:privacy", _type="set", to="s.whatsapp.net")
        self.setSetPrivacyListProps(blockedJids)

    def setSetPrivacyListProps(self, blockedJids):
        assert type(blockedJids) is list, "Expected blockedJids to be list"
        self.blockedJids = blockedJids

    @staticmethod
    def fromProtocolTreeNode(node):
        entity = IqProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = SetPrivacyListIqProtocolEntity
        items = node.getChild("query").getChild("list")
        blockedJids = []
        for item in items.getAllChildren():
            blockedJids.append(item['value'])
        entity.setSetPrivacyListProps(blockedJids)
        return entity

    def toProtocolTreeNode(self):
        node = super(SetPrivacyListIqProtocolEntity, self).toProtocolTreeNode()
        queryNode = ProtocolTreeNode("query")
        listNode = ProtocolTreeNode("list", {"name": "default"})
        for i, jid in enumerate(self.blockedJids):
            order = str(i + 1)
            item = ProtocolTreeNode("item",
                    {"type":"jid", "value":jid, "action":"deny", "order":order})
            listNode.addChild(item)
        queryNode.addChild(listNode)
        node.addChild(queryNode)
        return node

	def __str__(self):
		out = super(SetPrivacyListIqProtocolEntity, self).__str__()
		out += 'blockedJids: %s' % ','.join(self.blockedJids)
		return out

