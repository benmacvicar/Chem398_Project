from new_era import PumpInterface
 
pi = PumpInterface()

pi = PumpInterface(port = 'COM4',rate_unit='ml/min', volume_unit='ml')
#pi.xmit_sequence('PH 1','FUN rAtE', 'VOL 3.0', 'RAT 3.0','DIR INF')
#pi.xmit_sequence('PH 2','FUN rAtE', 'VOL 3.0', 'RAT 3.0','DIR INF')
pi.xmit_sequence('VER')
pi.run()
