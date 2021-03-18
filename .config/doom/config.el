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
(setq doom-font (font-spec :family "JetBrains Mono" :size 16))

;; Theme selection
(setq doom-theme 'doom-dracula)

;; Column fitting
(setq-default fill-column 80)

;; Centered cursor mode settings
(setq ccm-recenter-at-end-of-file t)

; ============ EDITING MODES ============ ;
; ==== Text mode ==== ;
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'text-mode-hook 'set-tex-input)
(add-hook 'text-mode-hook 'display-nums-white)
(add-hook 'text-mode-hook 'display-fill-column-indicator-mode)
(add-hook 'text-mode-hook 'centered-cursor-mode)

; ==== Programming mode ==== ;
(add-hook 'prog-mode-hook 'display-nums-white)
(add-hook 'prog-mode-hook 'flycheck-mode)
(add-hook 'prog-mode-hook 'display-fill-column-indicator-mode)
(add-hook 'prog-mode-hook 'centered-cursor-mode)

; ==== LaTeX mode ==== ;
;; Turn on reftex https://bit.ly/3gIgKHD
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)
(setq reftex-plug-into-AUCTeX t)

; Default bibliography
(setq reftex-default-bibliography "/home/juanscr/juanscr/jsc/backups/ref.bib")
(add-hook 'LaTeX-mode-hook 'no-tex-input)

; ==== Emacs IPython notebook ==== ;
;; Inline images notebook https://bit.ly/2YNUoy3
(setq ein:output-area-inlined-images t)

;; Enable undo https://bit.ly/31FfBvZ
(setq ein:worksheet-enable-undo t)

; ==== Org mode ==== ;
(require 'org)

; Increase size of equations https://bit.ly/3gliSF3
(setq org-format-latex-options (plist-put
org-format-latex-options :scale 2.0))

;; Do not have input method in org mode
(add-hook 'org-mode-hook 'no-tex-input)

; ============ IDE BEHAVIOR ============ ;
; ==== Company mode ==== ;
(setq company-idle-delay 0)
(setq company-show-numbers t)

; Additional backends
(require 'company-lsp)
(push 'company-lsp company-backends)

; Irony mode for C and C++
(add-hook 'c++-mode-hook 'irony-mode)
(add-hook 'c-mode-hook 'irony-mode)
(add-hook 'irony-mode-hook 'irony-cdb-autosetup-compile-options)

; Jedi mode for python
(defun python-jedi ()
  (add-to-list 'company-backends 'company-jedi))
(add-hook 'python-mode-hook 'python-jedi)

;; Activate LSP in all python buffers
(add-hook 'python-mode-hook #'lsp)

; ==== Julia mode ==== ;
(add-hook 'julia-mode-hook 'set-tex-input)
