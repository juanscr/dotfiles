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
(setq doom-font (font-spec :family "JetBrainsMono Nerd Font" :size 12))

;; Theme selection
(setq doom-theme 'doom-dracula)

;; Column fitting
(setq-default fill-column 88)
(setq-default display-fill-column-indicator-character ?|)

;; Centered cursor mode settings
(setq ccm-recenter-at-end-of-file t)

;; Modeline settings
(setq all-the-icons-scale-factor 1.1)
(after! doom-modeline
  (doom-modeline-def-modeline 'main '(bar matches buffer-info
    remote-host buffer-position parrot selection-info)
    '(misc-info minor-modes checker input-method buffer-encoding
    major-mode process vcs " ")))

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
(add-hook 'prog-mode-hook 'flyspell-prog-mode)

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
;; LSP with no autoguess
(setq-default lsp-auto-guess-root nil)

; ==== Company mode ==== ;
(setq company-idle-delay 0)
(setq company-show-numbers t)

; LSP for Rust
(after! rustic
  (setq rustic-lsp-server 'rls))

;; Julia LSP
(setq lsp-julia-package-dir nil)
(setq lsp-julia-default-environment "~/.julia/environments/v1.6/")
(setq lsp-enable-folding t)
(setq lsp-julia-flags `("-J/home/juanscr/.julia/environments/languageserver.so"
                        "--startup-file=no"
                        "--history-file=no"))
