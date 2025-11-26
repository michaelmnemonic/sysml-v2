{
  description = "Experiements with python";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    sysml-v2.url = "github:DLR-FT/sysml-v2-nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      sysml-v2,
    }:
    let
      # Define 'forAllSystems' for properties that shall be build for x86_64 *and* aarch64
      systems = [
        "x86_64-linux"
        "aarch64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
      pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
    in
    {
      packages = forAllSystems (system: {
        pysysml2 = pkgs.${system}.python3Packages.buildPythonPackage rec {
          pname = "pysysml2";
          version = "0.1.1";
          pyproject = true;

          src = pkgs.${system}.fetchFromGitHub {
            owner = "DAF-Digital-Transformation-Office";
            repo = "PySysML2";
            rev = "6dfaf83ebe8abe2c988a178e105e73c7e9c56fdf";
            hash = "sha256-i6Fey5dcSX0xMJJMTmHIdBgGWXUpgxP1DXA2JShQCQQ=";
          };

          dontCheckRuntimeDeps = true; # disable dependency check --> probably not a good idea

          dependencies = with pkgs.${system}.python313Packages; [
            poetry-core
            anytree
            graphviz
            numpy
            pandas
            openpyxl
            antlr4-python3-runtime
            typer
          ];
        };
      });

      devShells = forAllSystems (system: {
        default = pkgs.${system}.mkShell {
          buildInputs = with pkgs.${system}; [
            # basics
            gitMinimal

            #python
            python313
            ruff
            python313Packages.jinja2
            python313Packages.anytree
            python313Packages.graphviz
            python313Packages.numpy
            python313Packages.pandas
            python313Packages.openpyxl
            python313Packages.antlr4-python3-runtime
            python313Packages.typer
            self.packages.${system}.pysysml2

            # sysml-v2 API server
            sysml-v2.outputs.packages.${system}.sysml-v2-api-server

            # nix
            nil
            alejandra
          ];
        };
      });
    };
}
