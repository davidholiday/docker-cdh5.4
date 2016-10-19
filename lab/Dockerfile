FROM ubuntu

LABEL dockerdash.dashname="test_dash_1" \
      dockerdash.category1="test_category_1" \
      dockerdash.category1.name="foo" \
      dockerdash.category1.port="22" \
      dockerdash.category1.attribute="web" \
      dockerdash.category2="test_category_2" \
      dockerdash.category2.name="moo" \
      dockerdash.category2.port="666"

RUN apt-get update && apt-get install -y iputils-ping traceroute
CMD bash
