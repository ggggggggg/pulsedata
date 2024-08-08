import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

root = Path(__file__).parent

@dataclass(frozen=True)
class PulseNoisePair:
    pulse_folder: Path
    noise_folder: Path

pulse_noise_ljh_pairs = {"20230626": PulseNoisePair(root/"20230626"/"0001",root/"20230626"/"0000")} 
off = {"ebit_20240722_0006": root/"ebit_20240722_0006",
       "ebit_20240723_0000": root/"ebit_20240723_0000"}
