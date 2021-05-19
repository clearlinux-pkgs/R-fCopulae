#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fCopulae
Version  : 3042.82.1
Release  : 27
URL      : https://cran.r-project.org/src/contrib/fCopulae_3042.82.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fCopulae_3042.82.1.tar.gz
Summary  : Rmetrics - Bivariate Dependence Structures with Copulae
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fBasics
Requires: R-fMultivar
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-fBasics
BuildRequires : R-fMultivar
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R

%description
manage, to investigate and to analyze bivariate financial returns by  
	Copulae. Included are the families of Archemedean, Elliptical, 
	Extreme Value, and Empirical Copulae.

%prep
%setup -q -c -n fCopulae
cd %{_builddir}/fCopulae

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589772169

%install
export SOURCE_DATE_EPOCH=1589772169
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fCopulae
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fCopulae
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fCopulae
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fCopulae || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fCopulae/DESCRIPTION
/usr/lib64/R/library/fCopulae/INDEX
/usr/lib64/R/library/fCopulae/Meta/Rd.rds
/usr/lib64/R/library/fCopulae/Meta/features.rds
/usr/lib64/R/library/fCopulae/Meta/hsearch.rds
/usr/lib64/R/library/fCopulae/Meta/links.rds
/usr/lib64/R/library/fCopulae/Meta/nsInfo.rds
/usr/lib64/R/library/fCopulae/Meta/package.rds
/usr/lib64/R/library/fCopulae/NAMESPACE
/usr/lib64/R/library/fCopulae/R/fCopulae
/usr/lib64/R/library/fCopulae/R/fCopulae.rdb
/usr/lib64/R/library/fCopulae/R/fCopulae.rdx
/usr/lib64/R/library/fCopulae/help/AnIndex
/usr/lib64/R/library/fCopulae/help/aliases.rds
/usr/lib64/R/library/fCopulae/help/fCopulae.rdb
/usr/lib64/R/library/fCopulae/help/fCopulae.rdx
/usr/lib64/R/library/fCopulae/help/paths.rds
/usr/lib64/R/library/fCopulae/html/00Index.html
/usr/lib64/R/library/fCopulae/html/R.css
/usr/lib64/R/library/fCopulae/obsolete/R/biv-binning.R
/usr/lib64/R/library/fCopulae/obsolete/R/biv-density.R
/usr/lib64/R/library/fCopulae/obsolete/R/biv-gridding.R
/usr/lib64/R/library/fCopulae/obsolete/R/builtin-adapt.R
/usr/lib64/R/library/fCopulae/obsolete/R/bv-dcauchy.R
/usr/lib64/R/library/fCopulae/obsolete/R/bv-delliptical.R
/usr/lib64/R/library/fCopulae/obsolete/R/bv-dnorm.R
/usr/lib64/R/library/fCopulae/obsolete/R/bv-dt.R
/usr/lib64/R/library/fCopulae/obsolete/R/mv-distributions.R
/usr/lib64/R/library/fCopulae/obsolete/R/mv-dsnorm.R
/usr/lib64/R/library/fCopulae/obsolete/R/mv-dst.R
/usr/lib64/R/library/fCopulae/obsolete/src/adapt2.f
/usr/lib64/R/library/fCopulae/obsolete/src/adapt_callback.c
/usr/lib64/R/library/fCopulae/tests/doRUnit.R
/usr/lib64/R/library/fCopulae/unitTests/Makefile
/usr/lib64/R/library/fCopulae/unitTests/runTests.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ArchimedeanCopulae.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ArchimedeanDependency.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ArchimedeanGenerator.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ArchimedeanModelling.R
/usr/lib64/R/library/fCopulae/unitTests/runit.EllipticalCopulae.R
/usr/lib64/R/library/fCopulae/unitTests/runit.EllipticalDependency.R
/usr/lib64/R/library/fCopulae/unitTests/runit.EllipticalGenerator.R
/usr/lib64/R/library/fCopulae/unitTests/runit.EllipticalModelling.R
/usr/lib64/R/library/fCopulae/unitTests/runit.EmpiricalCopulae.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ExtremeValueCopulae.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ExtremeValueDependency.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ExtremeValueModelling.R
/usr/lib64/R/library/fCopulae/unitTests/runit.ExtrmeValueGenerator.R
/usr/lib64/R/library/fCopulae/unitTests/runit.aaaCopulaClass.R
