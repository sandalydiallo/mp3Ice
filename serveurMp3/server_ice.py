# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.7.0
#
# <auto-generated>
#
# Generated from file `server.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module app
_M_app = Ice.openModule('app')
__name__ = 'app'

if 'music' not in _M_app.__dict__:
    _M_app.music = Ice.createTempClass()
    class music(object):
        def __init__(self, name='', genre='', author='', url=''):
            self.name = name
            self.genre = genre
            self.author = author
            self.url = url

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.genre)
            _h = 5 * _h + Ice.getHash(self.author)
            _h = 5 * _h + Ice.getHash(self.url)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_app.music):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.genre is None or other.genre is None:
                    if self.genre != other.genre:
                        return (-1 if self.genre is None else 1)
                else:
                    if self.genre < other.genre:
                        return -1
                    elif self.genre > other.genre:
                        return 1
                if self.author is None or other.author is None:
                    if self.author != other.author:
                        return (-1 if self.author is None else 1)
                else:
                    if self.author < other.author:
                        return -1
                    elif self.author > other.author:
                        return 1
                if self.url is None or other.url is None:
                    if self.url != other.url:
                        return (-1 if self.url is None else 1)
                else:
                    if self.url < other.url:
                        return -1
                    elif self.url > other.url:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_app._t_music)

        __repr__ = __str__

    _M_app._t_music = IcePy.defineStruct('::app::music', music, (), (
        ('name', (), IcePy._t_string),
        ('genre', (), IcePy._t_string),
        ('author', (), IcePy._t_string),
        ('url', (), IcePy._t_string)
    ))

    _M_app.music = music
    del music

if '_t_tab' not in _M_app.__dict__:
    _M_app._t_tab = IcePy.defineSequence('::app::tab', (), _M_app._t_music)

if '_t_file' not in _M_app.__dict__:
    _M_app._t_file = IcePy.defineSequence('::app::file', (), IcePy._t_byte)

_M_app._t_Server = IcePy.defineValue('::app::Server', Ice.Value, -1, (), False, True, None, ())

if 'ServerPrx' not in _M_app.__dict__:
    _M_app.ServerPrx = Ice.createTempClass()
    class ServerPrx(Ice.ObjectPrx):

        def addDocument(self, music, context=None):
            return _M_app.Server._op_addDocument.invoke(self, ((music, ), context))

        def addDocumentAsync(self, music, context=None):
            return _M_app.Server._op_addDocument.invokeAsync(self, ((music, ), context))

        def begin_addDocument(self, music, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.Server._op_addDocument.begin(self, ((music, ), _response, _ex, _sent, context))

        def end_addDocument(self, _r):
            return _M_app.Server._op_addDocument.end(self, _r)

        def removeDocument(self, name, context=None):
            return _M_app.Server._op_removeDocument.invoke(self, ((name, ), context))

        def removeDocumentAsync(self, name, context=None):
            return _M_app.Server._op_removeDocument.invokeAsync(self, ((name, ), context))

        def begin_removeDocument(self, name, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.Server._op_removeDocument.begin(self, ((name, ), _response, _ex, _sent, context))

        def end_removeDocument(self, _r):
            return _M_app.Server._op_removeDocument.end(self, _r)

        def displayListMusic(self, context=None):
            return _M_app.Server._op_displayListMusic.invoke(self, ((), context))

        def displayListMusicAsync(self, context=None):
            return _M_app.Server._op_displayListMusic.invokeAsync(self, ((), context))

        def begin_displayListMusic(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.Server._op_displayListMusic.begin(self, ((), _response, _ex, _sent, context))

        def end_displayListMusic(self, _r):
            return _M_app.Server._op_displayListMusic.end(self, _r)

        def searchDocument(self, attribute, name, context=None):
            return _M_app.Server._op_searchDocument.invoke(self, ((attribute, name), context))

        def searchDocumentAsync(self, attribute, name, context=None):
            return _M_app.Server._op_searchDocument.invokeAsync(self, ((attribute, name), context))

        def begin_searchDocument(self, attribute, name, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.Server._op_searchDocument.begin(self, ((attribute, name), _response, _ex, _sent, context))

        def end_searchDocument(self, _r):
            return _M_app.Server._op_searchDocument.end(self, _r)

        def downloadDocument(self, music, context=None):
            return _M_app.Server._op_downloadDocument.invoke(self, ((music, ), context))

        def downloadDocumentAsync(self, music, context=None):
            return _M_app.Server._op_downloadDocument.invokeAsync(self, ((music, ), context))

        def begin_downloadDocument(self, music, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.Server._op_downloadDocument.begin(self, ((music, ), _response, _ex, _sent, context))

        def end_downloadDocument(self, _r):
            return _M_app.Server._op_downloadDocument.end(self, _r)

        def testLibvlcPlayer(self, context=None):
            return _M_app.Server._op_testLibvlcPlayer.invoke(self, ((), context))

        def testLibvlcPlayerAsync(self, context=None):
            return _M_app.Server._op_testLibvlcPlayer.invokeAsync(self, ((), context))

        def begin_testLibvlcPlayer(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.Server._op_testLibvlcPlayer.begin(self, ((), _response, _ex, _sent, context))

        def end_testLibvlcPlayer(self, _r):
            return _M_app.Server._op_testLibvlcPlayer.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_app.ServerPrx.ice_checkedCast(proxy, '::app::Server', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_app.ServerPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::app::Server'
    _M_app._t_ServerPrx = IcePy.defineProxy('::app::Server', ServerPrx)

    _M_app.ServerPrx = ServerPrx
    del ServerPrx

    _M_app.Server = Ice.createTempClass()
    class Server(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::app::Server')

        def ice_id(self, current=None):
            return '::app::Server'

        @staticmethod
        def ice_staticId():
            return '::app::Server'

        def addDocument(self, music, current=None):
            raise NotImplementedError("servant method 'addDocument' not implemented")

        def removeDocument(self, name, current=None):
            raise NotImplementedError("servant method 'removeDocument' not implemented")

        def displayListMusic(self, current=None):
            raise NotImplementedError("servant method 'displayListMusic' not implemented")

        def searchDocument(self, attribute, name, current=None):
            raise NotImplementedError("servant method 'searchDocument' not implemented")

        def downloadDocument(self, music, current=None):
            raise NotImplementedError("servant method 'downloadDocument' not implemented")

        def testLibvlcPlayer(self, current=None):
            raise NotImplementedError("servant method 'testLibvlcPlayer' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_app._t_ServerDisp)

        __repr__ = __str__

    _M_app._t_ServerDisp = IcePy.defineClass('::app::Server', Server, (), None, ())
    Server._ice_type = _M_app._t_ServerDisp

    Server._op_addDocument = IcePy.Operation('addDocument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_app._t_music, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    Server._op_removeDocument = IcePy.Operation('removeDocument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    Server._op_displayListMusic = IcePy.Operation('displayListMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_app._t_tab, False, 0), ())
    Server._op_searchDocument = IcePy.Operation('searchDocument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_app._t_tab, False, 0), ())
    Server._op_downloadDocument = IcePy.Operation('downloadDocument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_app._t_music, False, 0),), (), ((), _M_app._t_file, False, 0), ())
    Server._op_testLibvlcPlayer = IcePy.Operation('testLibvlcPlayer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_app.Server = Server
    del Server

# End of module app
