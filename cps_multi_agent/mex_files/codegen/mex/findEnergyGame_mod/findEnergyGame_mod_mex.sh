MATLAB="/usr/local/MATLAB/R2014a"
Arch=glnxa64
ENTRYPOINT=mexFunction
MAPFILE=$ENTRYPOINT'.map'
PREFDIR="/home/prasanna/.matlab/R2014a"
OPTSFILE_NAME="./mexopts.sh"
. $OPTSFILE_NAME
COMPILER=$CC
. $OPTSFILE_NAME
echo "# Make settings for findEnergyGame_mod" > findEnergyGame_mod_mex.mki
echo "CC=$CC" >> findEnergyGame_mod_mex.mki
echo "CFLAGS=$CFLAGS" >> findEnergyGame_mod_mex.mki
echo "CLIBS=$CLIBS" >> findEnergyGame_mod_mex.mki
echo "COPTIMFLAGS=$COPTIMFLAGS" >> findEnergyGame_mod_mex.mki
echo "CDEBUGFLAGS=$CDEBUGFLAGS" >> findEnergyGame_mod_mex.mki
echo "CXX=$CXX" >> findEnergyGame_mod_mex.mki
echo "CXXFLAGS=$CXXFLAGS" >> findEnergyGame_mod_mex.mki
echo "CXXLIBS=$CXXLIBS" >> findEnergyGame_mod_mex.mki
echo "CXXOPTIMFLAGS=$CXXOPTIMFLAGS" >> findEnergyGame_mod_mex.mki
echo "CXXDEBUGFLAGS=$CXXDEBUGFLAGS" >> findEnergyGame_mod_mex.mki
echo "LD=$LD" >> findEnergyGame_mod_mex.mki
echo "LDFLAGS=$LDFLAGS" >> findEnergyGame_mod_mex.mki
echo "LDOPTIMFLAGS=$LDOPTIMFLAGS" >> findEnergyGame_mod_mex.mki
echo "LDDEBUGFLAGS=$LDDEBUGFLAGS" >> findEnergyGame_mod_mex.mki
echo "Arch=$Arch" >> findEnergyGame_mod_mex.mki
echo OMPFLAGS= >> findEnergyGame_mod_mex.mki
echo OMPLINKFLAGS= >> findEnergyGame_mod_mex.mki
echo "EMC_COMPILER=gcc" >> findEnergyGame_mod_mex.mki
echo "EMC_CONFIG=optim" >> findEnergyGame_mod_mex.mki
"/usr/local/MATLAB/R2014a/bin/glnxa64/gmake" -B -f findEnergyGame_mod_mex.mk
