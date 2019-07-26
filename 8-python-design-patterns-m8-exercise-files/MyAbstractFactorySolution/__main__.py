from factories.saver_factory import SaverFactory
from factories.investor_factory import InvestorFactory


for factory in InvestorFactory, SaverFactory:
    customer = factory.create_commercial()
    customer = customer('Weyland Yutani')
    customer.report_type()
    customer = factory.create_government()
    customer = customer('Danish Health Department')
    customer.report_type()
    customer = factory.create_retail()
    customer = customer('André Fettouhi')
    customer.report_type()
