# import polars as pl
# from backend import Helper
# from backend.us import states as sts
# from gui import app
import datetime
from backend.SecondaryData import EIADataRetriever
# from backend.SecondaryData import CensusDataRetriever

# from backend.RedfinSearcher import RedfinSearcher as rfs

if __name__ == "__main__":
    # gui_app = app.App()
    # gui_app.mainloop()
    eia = EIADataRetriever()
    print(
        eia.monthly_price_per_million_btu_by_energy_type(
            EIADataRetriever.EnergyTypes.NATURAL_GAS,
            "CA",
            datetime.date(2022, 1, 1),
            datetime.date(2023, 1, 1),
        )
    )
    # state = sts.lookup("MS")
    # print(Helper.get_census_report_url_page(state.name))
    # c = CensusAPI()
    # print(c.get_acs5_subject_table_group_for_zcta_by_year("S1901", "2019"))
    # print(c.get_acs5_profile_table_group_for_zcta_by_year("DP05", "2019"))
