pkgname=newpkg-qml
pkgver=0.1
pkgrel=1
pkgdesc=""
arch=('aarch64' 'x86_64')
url=""
license=('GPL')
groups=()
depends=('python-es2-pyqt5' 'mauikit' 'python-opengl' 'qt5-es2-multimedia' 'qt5-es2-declarative' 'qt5-webkit' 'qt5-tools' 'mauikit' 'glew')
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
  export pkgname="main"
  echo $pkgdiyu
  export viewname="view.qml"
  export pkgsrc="src"
  mkdir -p $pkgdir
  pyrcc5 qml.qrc -o ${pkgname}_view.py
  install -Dm755 ${pkgname}_view.py "$pkgdir/usr/share/$pkgname/${pkgname}_view.py"
  install -Dm755 ${pkgname}.py "$pkgdir/usr/share/$pkgname/${pkgname}.py"
  install -Dm755 ${pkgname}.py "$pkgdir/usr/bin/${pkgname}"
  install -Dm755 ${pkgname}_view.py "$pkgdir/usr/bin/${pkgname}_view.py"
  install -Dm755 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm755 qml/$viewname "$pkgdir/usr/share/$pkgname/$viewname"
}
