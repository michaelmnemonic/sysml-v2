{
  description = "Experiement with SysML v. 2.0";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: {

  devShell.aarch64-linux = nixpkgs.legacyPackages.aarch64-linux.pkgs.mkShell {
      buildInputs = with nixpkgs.legacyPackages.aarch64-linux.pkgs; [
        jdk23_headless
        conda
      ];
  };
};
}
