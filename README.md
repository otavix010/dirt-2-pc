# DiRT 2 — port nativo para PC

Port do **DiRT 2** (Xbox 360) por **recompilação estática**: o código PowerPC do jogo é traduzido para C++ e compilado como um programa de Windows. Não há emulador de CPU rodando o jogo. A parte gráfica usa o runtime da [ReXGlue](https://github.com/rexglue/rexglue-sdk), derivado do [Xenia](https://xenia.jp).

**Nada do jogo vem neste repositório.** O port é gerado no seu PC a partir da sua própria cópia (a imagem `.iso` do disco). O código traduzido também é gerado aí e nunca é distribuído.

O runtime vem de uma compilação própria da ReXGlue com o AMD FidelityFX e correções do port ([otavix010/rexglue-sdk-ffx](https://github.com/otavix010/rexglue-sdk-ffx)), porque a oficial não traz o FidelityFX. Entre as correções está a da escala de resolução no D3D12, que derrubava o jogo acima de 1x.

O jeito mais fácil de jogar é pelo [Otavix Launcher](https://github.com/otavix010/otavix-launcher), que baixa este port, pede a sua `.iso`, gera tudo e cuida das opções.

## O que o port acrescenta

| | Xbox 360 | Port |
|--|--|--|
| Taxa de quadros | 30 fps | **60** fps (quadros reais) |
| Resolução interna | 720p | 720p, **1440p** ou 4K |
| Ampliação para a tela | — | AMD FSR 1, AMD CAS, FSR 3 temporal (experimental) ou bilinear, com nitidez ajustável |
| Anti-aliasing | o do jogo | o do jogo, mais FXAA opcional |
| Filtro anisotrópico | o do jogo | até 16x |
| Contador de fps | — | opcional, no canto da tela |

DLSS e XeSS não entram: os dois precisam de vetores de movimento, que os jogos de Xbox 360 não fornecem. O ganho de nitidez vem da resolução interna (supersampling de verdade), e a fluidez vem dos fps reais.

## Gerar à mão (sem o launcher)

Precisa do **Visual Studio 2022 Build Tools** com "Desenvolvimento para desktop com C++" e "C++ CMake tools for Windows". O gerador baixa o resto: o SDK da ReXGlue e o Clang (LLVM) portátil, numa pasta `_ferramentas` ao lado do port.

```powershell
.\gerar.ps1 -Iso "D:\Jogos\Dirt 2 (USA, Europe).iso"
.\jogar.cmd
```

O port foi feito a partir do **DiRT 2 (USA, Europe)**. O gerador confere o `default.xex` da sua `.iso` (SHA-1 `cdcbe29702fbf18e3e63002096d94d081cbf488f`) e avisa se for outra versão.

## Opções

Ficam em `dirt2.toml` ao lado do executável, ou no arquivo indicado pela variável `PORT_OPCOES`. O launcher grava em `opcoes.toml`. Cada uma também vale na linha de comando (`--fps 120`) ou como variável de ambiente (`REX_FPS=120`).

| Opção | Valores | Padrão |
|--|--|--|
| `fps` | 30, 60 | 60 |
| `resolution_scale` | 1 (720p), 2 (1440p), 3 (4K) | 2 |
| `filtro` | `fsr`, `cas`, `fsr3` (temporal, experimental), `bilinear` | `fsr` |
| `nitidez` | 0 a 100 | 70 |
| `swap_post_effect` | `none`, `fxaa`, `fxaa_extreme` | `none` |
| `anisotropic_override` | -1 (o do jogo), 3 (4x), 4 (8x), 5 (16x) | 5 |
| `fullscreen` | `true`, `false` | `true` |
| `monitor` | 0 (padrão), 1, 2... | 0 |
| `mostrar_fps` | `true`, `false` | `false` |
| `volume` | 0 a 100 | 100 |
| `vibration` | `true`, `false` | `true` |
| `zona_morta_esquerda`, `zona_morta_direita` | 0 a 50 (%) | 0 |
| `user_language` | 1 inglês, 3 alemão, 4 francês, 5 espanhol, 6 italiano | 1 |
| `iso` | caminho da `.iso` | — |

## Como funciona

- `config/funcoes.toml`: as funções que a análise estática não acha sozinha: chamadas só por ponteiro (nos dados ou com o endereço montado no código) ou fora do alcance da análise. `config/ganchos.toml`: os ganchos no código do jogo. `config/jogo.txt`: a versão do jogo que o gerador confere.
- `src/dirt2_app.h`: a unidade de cache (`cache:`) numa pasta ao lado dos saves, onde o jogo guarda replays e flashbacks: o `XMountUtilityDrive` do jogo é trocado por uma versão que monta a pasta (a ReXGlue responde às partições de cache com um dispositivo nulo, e a montagem original desistia).
- `config/ganchos.toml`: o intervalo de apresentação de 2 vblanks (30 fps) vira 1 a 60 fps; o cronômetro das corridas segue o tempo real.
- O brilho: o jogo mede a exposição lendo pela CPU a imagem que acabou de desenhar. Sem essa leitura, que a ReXGlue deixa desligada por padrão, todas as cenas e menus saíam escuros. O port liga a leitura do quadro anterior (`readback_resolve = fast`, como as notas de compatibilidade do Xenia indicam), que dá o brilho certo a 60 fps.
- `src/port/`: a base comum dos ports de Xbox 360 (a mesma em todos): opções de imagem, contador de fps, leitura da `.iso`, a trava que corrige uma corrida na entrada de controles da ReXGlue, `falha.log` com a pilha em caso de falha.

Para desenvolver: `build.cmd` compila; `scripts/rodar.py` roda numa janela com prints, o fps de cada segundo e um controle roteirizado (`PORT_PAD`; para começar um jogo novo: `--pad 12:START,20:START,25-150@3:A`); `scripts/tecla.py` aperta botões no jogo em execução; `scripts/varrer_ponteiros.py` e `scripts/desmontar.py` ajudam a achar funções.

## Créditos

- [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk): recompilador estático e runtime de Xbox 360 (BSD-3).
- [Xenia](https://github.com/xenia-project/xenia): o emulador em que o runtime se baseia (BSD-3).

DiRT 2 é marca da Codemasters. Este projeto não tem relação com ela nem com a Microsoft.

## Licença

O código deste repositório está sob a licença MIT (`LICENSE`). O SDK e o runtime têm a licença própria deles (BSD-3).
