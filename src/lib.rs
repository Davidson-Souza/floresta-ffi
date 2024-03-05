uniffi::include_scaffolding!("floresta");

use florestad::Florestad as ActualFlorestad;

pub struct Florestad(ActualFlorestad);

impl Florestad {
    pub fn new() -> Self {
        let config = florestad::run::Config {
            network: florestad::cli::Network::Signet,
            ..Default::default()
        };

        Self(config.into())
    }

    pub fn run(&self) {
        self.0.start();
    }

}
