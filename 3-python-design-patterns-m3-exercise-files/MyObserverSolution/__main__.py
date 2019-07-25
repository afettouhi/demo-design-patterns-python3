from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# Report on current KPI values with added push support
kpis = KPIs()
with CurrentKPIs(kpis), ForecastKPIs(kpis):
    kpis.set_kpis(25, 10, 5)
    kpis.set_kpis(100, 50, 30)
    kpis.set_kpis(50, 10, 20)

print('\n***Outside of context manager with added push support.***\n\n')
kpis.set_kpis(150, 110, 120)
