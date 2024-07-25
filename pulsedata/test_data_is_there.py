import pulsedata

def test_data_is_there():
    for k,v in pulsedata.off.items():
        assert v.is_dir()

    for k,v in pulsedata.pulse_noise_ljh_pairs.items():
        assert v.pulse_folder.is_dir()
        assert v.noise_folder.is_dir()