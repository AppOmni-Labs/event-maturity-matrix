.PHONY: create_product

create_product:
	@python scripts/create_product.py

update_event_sources:
	@python scripts/update_event_sources.py