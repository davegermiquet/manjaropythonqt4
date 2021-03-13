pkgname=newpkg-qml
pkgver=0.1
pkgrel=1
pkgdesc=""
arch=('aarch64' 'x86_64')
url=""
license=('GPL')
groups=()
depends=('python-es2-pyqt5' 'kirigami2' 'glew')
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
  export pkgname="main.py"
  export pkgdir="../myexamplepkg"
  export viewname="view.qml"
  export pkgsrc="src"
  mkdir -p $pkgdir
  install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
  install -Dm755 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm755 $pkgname "$pkgdir/usr/share/$pkgname/$pkgname"
  install -Dm755 $viewname "$pkgdir/usr/share/$pkgname/$viewname"
}
