-- Packer installation
vim.cmd [[packadd packer.nvim]]

-- Packages dependencies
return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'

  -- Dracula theme
  use 'Mofiqul/dracula.nvim'

  -- Fuzzy finder
  use {
  	'nvim-telescope/telescope.nvim', 
  	tag = '0.1.1',
  	requires = { {'nvim-lua/plenary.nvim'} }
  }

  -- File project explore
  use {
        'nvim-treesitter/nvim-treesitter',
        run = ':TSUpdate'
  }
end)
