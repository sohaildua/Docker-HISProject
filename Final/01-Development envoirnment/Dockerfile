# escape=`

# To know windows servercore
ARG WIN_VER="ltsc2019"
FROM mcr.microsoft.com/windows/servercore:$WIN_VER

# Setup Envoirnment variables
ENV chocolateyUseWindowsCompression "true"
ENV RUST_TOOLCHAIN="1.30.1"

# To install microsoft build tools
ADD https://aka.ms/vs/16/release/vs_buildtools.exe C:\TEMP\vs_buildtools.exe
ADD https://win.rustup.rs/x86_64 C:\TEMP\rustup-init.exe
ADD https://chocolatey.org/install.ps1 C:\TEMP\choco-install.ps1

# Let's be explicit about the shell that we're going to use.
SHELL ["cmd", "/S", "/C"]

# To install Rust
RUN powershell C:\TEMP\choco-install.ps1
RUN powershell C:\TEMP\rustup-init.exe -y --default-toolchain $env:RUST_TOOLCHAIN

RUN rustup toolchain install nightly-2018-08-01
RUN rustup default nightly
RUN rustup update