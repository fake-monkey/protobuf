set install_dir=build_msvc\install
copy conanfile.py %install_dir%\
conan export-pkg %install_dir% -s build_type=Release
pause
