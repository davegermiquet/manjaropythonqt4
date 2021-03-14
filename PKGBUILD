pkgname=newpkg-qml
pkgver=0.1
pkgrel=1
pkgdesc=""
arch=('aarch64' 'x86_64')
url=""
license=('GPL')
groups=()
depends=('python-es2-pyqt5' 'mauikit' 'glew')
makedepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
noextract=()
md5sums=() #generate with 'makepkg -g'

package() {
  export pkgname="main"l
  export pkgdir="../myexamplepkg"
  export viewname="view.qml"
  export pkgsrc="src"
  mkdir -p $pkgdir
  pyrcc5 qml.qrc -o ${pkgname}_view.py
  install -Dm755 ${pkgname}_view.py "$pkgdir/usr/share/$pkgname/${pkgname}_view.py"
  install -Dm755 ${pkgname}.py "$pkgdir/usr/share/$pkgname/${pkgname}.py"
  install -Dm755 ${pkgname}.py "$pkgdir/usr/bin/${pkgname}.py"
  install -Dm755 ${pkgname}_view.py "$pkgdir/usr/bin/${pkgname}_view.py"
  install -Dm755 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm755 qml/$viewname "$pkgdir/usr/share/$pkgname/$viewname"
}
