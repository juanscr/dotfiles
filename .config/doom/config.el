; ============ BASIC FUNCTIONS ============ ;
;; TeX input method
(defun set-tex-input ()
  (set-input-method "TeX"))

;; Deactivate input method when active
(defun no-tex-input ()
  (toggle-input-method))

;; Line numbers
(defun display-nums-white()
  (setq display-line-numbers t)
  (setq show-trailing-whitespace t))

; ============ BASE EDITOR ============ ;
;; Font size
(setq doom-font (font-spec :family "monospace" :size 15))

;; Theme selection
(setq doom-theme 'doom-dracula)

; ============ MODES ============ ;
; ==== Text mode ==== ;
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'text-mode-hook 'set-tex-input)
(add-hook 'text-mode-hook 'display-nums-white)

; ==== Programming mode ==== ;
(add-hook 'prog-mode-hook 'display-nums-white)

; ==== LaTeX mode ==== ;
;; Turn on reftex https://bit.ly/3gIgKHD
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)
(setq reftex-plug-into-AUCTeX t)

; ==== Emacs IPython notebook ==== ;
;; Inline images notebook https://github.com/hlissner/doom-emacs/issues/2545
(setq ein:output-area-inlined-images t)

; ==== Org mode ==== ;
(require 'org)

; Increase size of equations https://bit.ly/3gliSF3
(setq org-format-latex-options (plist-put
org-format-latex-options :scale 2.0))

;; Do not have input method in org mode
(add-hook 'org-mode-hook 'no-tex-input)
