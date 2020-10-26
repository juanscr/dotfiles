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

;; Autocompletion with company
(setq company-idle-delay 0)
(setq company-show-numbers t)

; ============ MODES ============ ;
; ==== Text mode ==== ;
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'text-mode-hook 'set-tex-input)
(add-hook 'text-mode-hook 'display-nums-white)

; ==== Programming mode ==== ;
(add-hook 'prog-mode-hook 'display-nums-white)
(add-hook 'prog-mode-hook 'flycheck-mode)

; ==== LaTeX mode ==== ;
;; Turn on reftex https://bit.ly/3gIgKHD
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)
(setq reftex-plug-into-AUCTeX t)

(add-hook 'LaTeX-mode-hook 'no-tex-input)

; ==== Emacs IPython notebook ==== ;
;; Inline images notebook https://bit.ly/2YNUoy3
(setq ein:output-area-inlined-images t)

;; Enable undo https://bit.ly/31FfBvZ
(setq-default ein:worksheet-enable-undo t)

; ==== Org mode ==== ;
(require 'org)

; Increase size of equations https://bit.ly/3gliSF3
(setq org-format-latex-options (plist-put
org-format-latex-options :scale 2.0))

;; Do not have input method in org mode
(add-hook 'org-mode-hook 'no-tex-input)

; ==== Irony mode ==== ;
(add-hook 'c++-mode-hook 'irony-mode)
(add-hook 'c-mode-hook 'irony-mode)
(add-hook 'irony-mode-hook 'irony-cdb-autosetup-compile-options)

; ==== Python mode ==== ;
(defun python-jedi ()
  (add-to-list 'company-backends 'company-jedi))
(add-hook 'python-mode-hook 'python-jedi)

; ==== Julia mode ==== ;
(add-hook 'julia-mode-hook 'set-tex-input)
