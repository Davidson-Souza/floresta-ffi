build:
	cargo build --lib --release

gen-python: build
	cargo run --bin uniffi-bindgen generate --language python src/floresta.udl --out-dir generated/python
