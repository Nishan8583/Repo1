'''For this script to run, ryu controller must be installed in the maachine
	This code was successfully run in Ubuntu 14.04 32 bit python3
	to run this script:
	username@machine# ryu-manager ~/path/to/script

'''

from ryu.base import app_manager  # THe main class needed to create a ryu application
from ryu.lib.packet import packet  # To parse packet
from ryu.controller.handler import set_ev_cls  # function is added to it in order to handle packet
from ryu.controller import ofp_event  # To use the different OpenFlow event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.ofproto import ofproto_v1_0
import array

class MyApp(app_manager.RyuApp):
	def __init__(self, *args, **kwargs):
		super(MyApp, self).__init__(*args, **kwargs)

	@set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
	def packet_in_handler(self,ev):
		print("Recieved an OpenFlow Packet_In Message")
		pkt = packet.Packet(array.array('B',ev.msg.data))
		for p in pkt.protocols:
			print(p)
			print("\n-----------------------NEW PACKET---------------------------\n")

			'''THe following code will much more clearer if the Openflow protocl is understood'''
			msg = ev.msg
			dp = msg.datapath
			ofp = dp.ofproto
			ofp_parser = dp.ofproto_parser

			actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]  # Preparing an action that the openflow switch will need perfomr
			out = ofp_parser.OFPPacketOut(datapath = dp, buffer_id = msg.buffer_id, in_port = msg.in_port, actions = actions)  # The Packet_OUT message
			dp.send_msg(out)  # Sending the message
