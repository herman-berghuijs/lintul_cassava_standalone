from pathlib import Path

cwd = Path.cwd()
input_dir = cwd / "input"
agro_dir = input_dir / "agro"
agro_fp = agro_dir / "Benue_2016_NfPfKf_agro.yaml"
crop_dir = input_dir / "crop"
crop_fp = crop_dir / "cassava.yaml"
conf_dir = input_dir / "config"
conf_fp_pp = conf_dir / "Lintul_cassava10_PP.conf"
conf_fp_wlp = conf_dir / "Lintul_cassava10_WLP.conf"
conf_fp_wnlp = conf_dir / "Lintul_cassava10_WNLP.conf"
site_dir = input_dir / "site"
site_fp = site_dir / "Benue_2016_NfPfKf_site.yaml"
soil_dir = input_dir / "soil"
soil_fp = soil_dir / "Benue_2016_soil.yaml"
weather_dir = input_dir / "weather"
weather_fn = "nig2"