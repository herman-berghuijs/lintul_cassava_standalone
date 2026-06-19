from pcse.base import ParameterProvider
from pcse.engine import Engine
from pcse.input import CABOWeatherDataProvider
from pathlib import Path
import input_file_paths as ifp
import pandas as pd
import yaml

def run_model_and_collect_output(agrod, parameters, wdp, modelconf_fp):
    model = Engine(parameters, wdp, agrod, config=modelconf_fp)
    model.run_till_terminate()
    output = model.get_output()
    df_out = pd.DataFrame(output)
    return df_out

def main():
    weather_fn = "nig2.016"
    station_id = 2

    with open(ifp.crop_fp) as f:
        cropd = yaml.safe_load(f.read())
    with open(ifp.agro_fp) as f:
        agrod = yaml.safe_load(f.read())
    with open(ifp.soil_fp) as f:
        soild = yaml.safe_load(f.read())
    with open(ifp.site_fp) as f:
        sited = yaml.safe_load(f.read())
    wdp = CABOWeatherDataProvider(fname="nig2", fpath=ifp.weather_dir)
    parameters = ParameterProvider(cropdata=cropd,
                                   sitedata=sited,
                                   soildata=soild)
    df_out_wlp = run_model_and_collect_output(agrod, parameters, wdp, ifp.conf_fp_wlp)
    df_out_pp = run_model_and_collect_output(agrod, parameters, wdp, ifp.conf_fp_pp)
    df_out_wnlp = run_model_and_collect_output(agrod, parameters, wdp, ifp.conf_fp_wnlp)



if __name__ == "__main__":
    main()
