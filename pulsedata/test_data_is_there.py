import pulsedata

def test_data_is_there():
    for k,v in pulsedata.off.items():
        assert v.is_dir()

    for k,v in pulsedata.pulse_noise_ljh_pairs.items():
        assert v.pulse_folder.is_dir()
        assert v.noise_folder.is_dir()


def test_can_open_files():
    open(pulsedata.off["ebit_20240722_0006"]/"20240722_run0006_chan1.off","rb")
    open(pulsedata.off["ebit_20240723_0000"]/"20240723_run0000_chan1.off","rb")