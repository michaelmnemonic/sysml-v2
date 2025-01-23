{
  description = "Experiement with SysML v. 2.0";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-24.11";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    pkgs = nixpkgs.legacyPackages.aarch64-linux.pkgs;
  in {
    devShell.aarch64-linux = pkgs.mkShell {
      buildInputs = with pkgs; [
        eclipses.eclipse-platform
        graphviz
      ];
    };
  };
}
