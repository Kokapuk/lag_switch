import pydivert
from config_manager import load_config
import threading

config = load_config()


def handle_drop_packets(enabled):
    with pydivert.WinDivert('outbound and ip.SrcAddr != 127.0.0.1') as w:
        for packet in w:
            if not enabled['value']:
                w.send(packet)
                continue

            for channel in config['ignore_channels']:
                port_match = packet.dst_port in range(
                    channel['port_range'][0], channel['port_range'][1])
                protocol_match = any(
                    x == packet.protocol[0] for x in channel['protocols'])

                if port_match and protocol_match:
                    w.send(packet)


def send_lag_packet(w, packet):
    w.send(packet)


def handle_lag_packets(enabled):
    with pydivert.WinDivert('inbound and ip.DstAddr != 127.0.0.1') as w:
        for packet in w:
            if not enabled['value']:
                w.send(packet)
                continue

            ignored = False

            for channel in config['ignore_channels']:
                port_match = packet.src_port in range(
                    channel['port_range'][0], channel['port_range'][1])
                protocol_match = any(
                    x == packet.protocol[0] for x in channel['protocols'])

                if port_match and protocol_match:
                    w.send(packet)
                    ignored = True

            if not ignored:
                threading.Timer(config['lag'] / 1000,
                                send_lag_packet, args=(w, packet)).start()
