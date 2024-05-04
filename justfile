export ARCH := "$(uname -m)"
export OS := "$(uname -s | tr '[:upper:]' '[:lower:]')"

build:
	cargo build --lib --release

gen-python: build
	cargo run --bin uniffi-bindgen generate --language python src/floresta.udl --out-dir generated/python

gen-tar: gen-python
    cp target/release/libflorestad_ffi.so generated/python/libuniffi_floresta.so
    tar cf "{{ARCH}}-{{OS}}.tar" generated/python/floresta.py generated/python/libuniffi_floresta.so
