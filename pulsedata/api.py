import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict

root = Path(__file__).parent

@dataclass(frozen=True)
class PulseNoisePair:
    pulse_folder: Path
    noise_folder: Path

pulse_noise_ljh_pairs: Dict[str, PulseNoisePair] = {"20230626": PulseNoisePair(root/"20230626"/"0001",root/"20230626"/"0000"),
                         "bessy_20240727": PulseNoisePair(root/"bessy_20240727"/"0002",root/"bessy_20240727"/"0000")} 
off: Dict[str, Path] = {"ebit_20240722_0006": root/"ebit_20240722_0006",
       "ebit_20240723_0000": root/"ebit_20240723_0000"}

parquet: Dict[str, Path] = {"truebq_202508_5um_Pu239.parquet": root/"truebq_202508"/"5umfoilPu239.parquet",
           "truebq_202508_20um_BLANK.parquet": root/"truebq_202508"/"20umfoilPu239_BLANK.parquet",
           "truebq_202508_20um_Pu239.parquet": root/"truebq_202508"/"20umfoilPu239.parquet"}
