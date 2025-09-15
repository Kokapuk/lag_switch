import pydivert
from config_manager import load_config
import threading

config = load_config()

IGNORE_CHANNELS = [
    {'ports': range(50000, 65536), 'protocols': [
        pydivert.Protocol.UDP]},  # DISCORD VOICES

    {'ports': range(27015, 27050), 'protocols': [
        pydivert.Protocol.UDP, pydivert.Protocol.TCP]},  # STEAM FRIENDS AND ACTIVITY
]


def handle_drop_packets(enabled):
    with pydivert.WinDivert('outbound and ip.SrcAddr != 127.0.0.1') as w:
        for packet in w:
            if not enabled['value']:
                w.send(packet)
                continue

            for channel in IGNORE_CHANNELS:
                if any(x == packet.protocol[0] for x in channel['protocols']) and packet.dst_port in channel['ports']:
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

            for channel in IGNORE_CHANNELS:
                if any(x == packet.protocol[0] for x in channel['protocols']) and packet.src_port in channel['ports']:
                    w.send(packet)
                    ignored = True

            if not ignored:
                threading.Timer(config['lag'] / 1000,
                                send_lag_packet, args=(w, packet)).start()
