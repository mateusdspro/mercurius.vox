"""
Indicador visual na tela quando gravando
Mostra ícone de microfone flutuante (similar ao macOS nativo)
"""

import threading
from AppKit import (
    NSApplication,
    NSWindow,
    NSWindowStyleMaskBorderless,
    NSBackingStoreBuffered,
    NSFloatingWindowLevel,
    NSColor,
    NSTextField,
    NSFont,
    NSMakeRect,
    NSScreen,
    NSView,
)
from PyObjCTools import AppHelper


class VisualIndicator:
    """Mostra ícone de microfone flutuante quando gravando"""
    
    def __init__(self):
        self.window = None
        self.is_visible = False
        self._initialized = False
    
    def _create_window(self):
        """Cria janela flutuante pequena"""
        if self._initialized:
            return
        
        try:
            screen = NSScreen.mainScreen()
            screen_frame = screen.frame()
            
            # Janela pequena no canto superior direito
            width = 80
            height = 80
            x = screen_frame.size.width - width - 20
            y = screen_frame.size.height - height - 60
            
            frame = NSMakeRect(x, y, width, height)
            
            self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
                frame,
                NSWindowStyleMaskBorderless,
                NSBackingStoreBuffered,
                False
            )
            
            self.window.setLevel_(NSFloatingWindowLevel)
            self.window.setOpaque_(False)
            self.window.setBackgroundColor_(NSColor.clearColor())
            self.window.setHasShadow_(True)
            self.window.setIgnoresMouseEvents_(True)
            
            # View com fundo
            content_view = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, width, height))
            content_view.setWantsLayer_(True)
            content_view.layer().setBackgroundColor_(
                NSColor.colorWithRed_green_blue_alpha_(0.1, 0.1, 0.1, 0.9).CGColor()
            )
            content_view.layer().setCornerRadius_(20)
            
            # Ícone de microfone (emoji)
            label = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 15, width, 50))
            label.setStringValue_("🎤")
            label.setBezeled_(False)
            label.setDrawsBackground_(False)
            label.setEditable_(False)
            label.setSelectable_(False)
            label.setFont_(NSFont.systemFontOfSize_(40))
            label.setAlignment_(1)  # Centro
            
            content_view.addSubview_(label)
            self.window.setContentView_(content_view)
            
            self._initialized = True
        except Exception as e:
            print(f"⚠️  Erro ao criar indicador visual: {e}")
    
    def show(self):
        """Mostra o indicador"""
        def _show():
            try:
                self._create_window()
                if self.window:
                    self.window.orderFront_(None)
                    self.is_visible = True
            except Exception:
                pass
        
        try:
            AppHelper.callAfter(_show)
        except Exception:
            pass
    
    def hide(self):
        """Esconde o indicador"""
        def _hide():
            try:
                if self.window:
                    self.window.orderOut_(None)
                    self.is_visible = False
            except Exception:
                pass
        
        try:
            AppHelper.callAfter(_hide)
        except Exception:
            pass






