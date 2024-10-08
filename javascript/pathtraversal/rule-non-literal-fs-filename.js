// License: MIT (c) GitLab Inc.

const fs = require('node:fs');
import fs2 from "fs";

function negative(argOne, argTwo) {
    
  // string args
  fs2.appendFile('foo', data, callback)
  fs.appendFileSync('foo', data)
  fs.chmod('foo', mode, callback)
  fs.chmodSync('foo', mode)
  fs.chown('foo', uid, gid, callback)
  fs.chownSync('foo', uid, gid)
  fs.createReadStream('foo')
  fs.createWriteStream('foo')
  fs.exists('foo', callback)
  fs.existsSync('foo', callback)
  fs.lchmod('foo', mode, callback)
  fs.lchmodSync('foo', mode)
  fs.lchown('foo', uid, gid, callback)
  fs.lchownSync('foo', uid, gid)
  fs.link('foo', 'bar', callback)
  fs.linkSync('foo', 'bar')
  fs.lstat('foo', callback)
  fs.lstatSync('foo')
  fs.mkdir('foo', callback)
  fs.mkdirSync('foo')
  fs.open('foo', callback)
  fs.openSync('foo')
  fs.readdir('foo', callback)
  fs.readdirSync('foo')
  fs.readFile('foo', callback)
  fs.readFileSync('foo')
  fs.readlink('foo', callback)
  fs.readlinkSync('foo')
  fs.realpath('foo', callback)
  fs.realpathSync('foo')
  fs.rename('foo', 'bar', callback)
  fs.renameSync('foo', 'bar')
  fs.rmdir('foo', callback)
  fs.rmdirSync('foo')
  fs.stat('foo', callback)
  fs.statSync('foo')
  fs.symlink('foo', 'bar', callback)
  fs.symlinkSync('foo', 'bar')
  fs.truncate('foo', callback)
  fs.truncateSync('foo')
  fs.unlink('foo', callback)
  fs.unlinkSync('foo')
  fs.unwatchFile('foo')
  fs.utimes('foo', callback)
  fs.utimesSync('foo')
  fs.watch('foo')
  fs.watchFile('foo', listener)
  fs.writeFile('foo', callback)
  fs.writeFileSync('foo')

  // constant string arguments
  strArgOne = 'foo'
  strArgTwo = 'bar'
  fs.appendFile(strArgOne, data, callback)
  fs.appendFileSync(strArgOne, data)
  fs.chmod(strArgOne, mode, callback)
  fs.chmodSync(strArgOne, mode)
  fs.chown(strArgOne, uid, gid, callback)
  fs.chownSync(strArgOne, uid, gid)
  fs.createReadStream(strArgOne)
  fs.createWriteStream(strArgOne)
  fs.exists(strArgOne, callback)
  fs.existsSync(strArgOne, callback)
  fs.lchmod(strArgOne, mode, callback)
  fs.lchmodSync(strArgOne, mode)
  fs.lchown(strArgOne, uid, gid, callback)
  fs.lchownSync(strArgOne, uid, gid)
  fs.link(strArgOne, strArgTwo, callback)
  fs.linkSync(strArgOne, strArgTwo)
  fs.lstat(strArgOne, callback)
  fs.lstatSync(strArgOne)
  fs.mkdir(strArgOne, callback)
  fs.mkdirSync(strArgOne)
  fs.open(strArgOne, callback)
  fs.openSync(strArgOne)
  fs.readdir(strArgOne, callback)
  fs.readdirSync(strArgOne)
  fs.readFile(strArgOne, callback)
  fs.readFileSync(strArgOne)
  fs.readlink(strArgOne, callback)
  fs.readlinkSync(strArgOne)
  fs.realpath(strArgOne, callback)
  fs.realpathSync(strArgOne)
  fs.rename(strArgOne, strArgTwo, callback)
  fs.renameSync(strArgOne, strArgTwo)
  fs.rmdir(strArgOne, callback)
  fs.rmdirSync(strArgOne)
  fs.stat(strArgOne, callback)
  fs.statSync(strArgOne)
  fs.symlink(strArgOne, strArgTwo, callback)
  fs.symlinkSync(strArgOne, strArgTwo)
  fs.truncate(strArgOne, callback)
  fs.truncateSync(strArgOne)
  fs.unlink(strArgOne, callback)
  fs.unlinkSync(strArgOne)
  fs.unwatchFile(strArgOne)
  fs.utimes(strArgOne, callback)
  fs.utimesSync(strArgOne)
  fs.watch(strArgOne)
  fs.watchFile(strArgOne, listener)
  fs.writeFile(strArgOne, callback)
  fs.writeFileSync(strArgOne)

  const notfs = require("test");
  notfs.appendFile(argOne, data, callback)
  notfs.appendFileSync(argOne, data)
  notfs.chmod(argOne, mode, callback)
  notfs.chmodSync(argOne, mode)
  notfs.chown(argOne, uid, gid, callback)
  notfs.chownSync(argOne, uid, gid)
  notfs.createReadStream(argOne)
  notfs.createWriteStream(argOne)
  notfs.exists(argOne, callback)
  notfs.existsSync(argOne, callback)
  notfs.lchmod(argOne, mode, callback)
  notfs.lchmodSync(argOne, mode)
  notfs.lchown(argOne, uid, gid, callback)
  notfs.lchownSync(argOne, uid, gid)
  notfs.link(argOne, argTwo, callback)
  notfs.linkSync(argOne, argTwo)
  notfs.lstat(argOne, callback)
  notfs.lstatSync(argOne)
  notfs.mkdir(argOne, callback)
  notfs.mkdirSync(argOne)
  notfs.open(argOne, callback)
  notfs.openSync(argOne)
  notfs.readdir(argOne, callback)
  notfs.readdirSync(argOne)
  notfs.readFile(argOne, callback)
  notfs.readFileSync(argOne)
  notfs.readlink(argOne, callback)
  notfs.readlinkSync(argOne)
  notfs.realpath(argOne, callback)
  notfs.realpathSync(argOne)
  notfs.rename(argOne, argTwo, callback)
  notfs.renameSync(argOne, argTwo)
  notfs.rmdir(argOne, callback)
  notfs.rmdirSync(argOne)
  notfs.stat(argOne, callback)
  notfs.statSync(argOne)
  notfs.symlink(argOne, argTwo, callback)
  notfs.symlinkSync(argOne, argTwo)
  notfs.truncate(argOne, callback)
  notfs.truncateSync(argOne)
  notfs.unlink(argOne, callback)
  notfs.unlinkSync(argOne)
  notfs.unwatchFile(argOne)
  notfs.utimes(argOne, callback)
  notfs.utimesSync(argOne)
  notfs.watch(argOne)
  notfs.watchFile(argOne, listener)
  notfs.writeFile(argOne, callback)
  notfs.writeFileSync(argOne)
}

function positive(argOne, argTwo) {
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.appendFile(argOne, data, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.appendFileSync(argOne, data)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.chmod(argOne, mode, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.chmodSync(argOne, mode)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.chown(argOne, uid, gid, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.chownSync(argOne, uid, gid)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.createReadStream(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.createWriteStream(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.exists(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.existsSync(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.lchmod(argOne, mode, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.lchmodSync(argOne, mode)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.lchown(argOne, uid, gid, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.lchownSync(argOne, uid, gid)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.link(argOne, argTwo, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.linkSync(argOne, argTwo)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.lstat(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.lstatSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.mkdir(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.mkdirSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.open(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.openSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.readdir(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.readdirSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.readFile(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.readFileSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.readlink(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.readlinkSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.realpath(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.realpathSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.rename(argOne, argTwo, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.renameSync(argOne, argTwo)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.rmdir(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.rmdirSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.stat(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.statSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.symlink(argOne, argTwo, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.symlinkSync(argOne, argTwo)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.truncate(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.truncateSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.unlink(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.unlinkSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.unwatchFile(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.utimes(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.utimesSync(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.watch(argOne)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.watchFile(argOne, listener)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.writeFile(argOne, callback)
  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs.writeFileSync(argOne)


  // ruleid: javascript_pathtraversal_rule-non-literal-fs-filename
  fs2.writeFileSync(argOne)
}
