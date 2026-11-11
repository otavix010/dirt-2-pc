<h1 align="center">DiRT 2 — port nativo para PC</h1>

<p align="center"><i>DiRT 2 (Xbox 360) — port nativo para PC por recompilação estática (Otavix Engine 360). Gera a partir da sua .iso.</i></p>

<p align="center">
  <a href="https://github.com/otavix010/dirt-2-pc/commits/main"><img alt="Última atualização" src="https://img.shields.io/github/last-commit/otavix010/dirt-2-pc?label=%C3%BAltima%20atualiza%C3%A7%C3%A3o"></a>
  <a href="LICENSE"><img alt="Licença" src="https://img.shields.io/github/license/otavix010/dirt-2-pc?label=licen%C3%A7a"></a>
  <a href="https://github.com/otavix010/otavix-launcher/releases/latest"><img alt="Baixar o Otavix Launcher" src="https://img.shields.io/badge/Otavix%20Launcher-baixar-b00020"></a>
  <img alt="Windows 10/11" src="https://img.shields.io/badge/Windows-10%2F11-0078d4">
  <img alt="Linux: não suportado no momento" src="https://img.shields.io/badge/Linux-n%C3%A3o%20suportado-lightgrey">
</p>

<p align="center">
  <a href="#o-que-o-port-acrescenta">O que o port acrescenta</a> ·
  <a href="#estado-dos-testes">Estado dos testes</a> ·
  <a href="#plataformas">Plataformas</a> ·
  <a href="#requisitos">Requisitos</a> ·
  <a href="#desempenho-medido">Desempenho</a> ·
  <a href="#perguntas-frequentes">Perguntas frequentes</a> ·
  <a href="#gerar-à-mão-sem-o-launcher">Gerar à mão (sem o launcher)</a> ·
  <a href="#opções">Opções</a> ·
  <a href="#como-funciona">Como funciona</a>
</p>

> [!IMPORTANT]
> **Para jogar, baixe o [Otavix Launcher](https://github.com/otavix010/otavix-launcher/releases/latest).** Ele baixa este port, pede a sua `.iso`, gera o jogo no seu PC e o mantém atualizado. Para relatar um problema ou pedir algo, use **"Reportar problema"** na página do jogo no launcher: o relatório já vai com o log e as configurações, e é por ele que as correções saem mais rápido.
>
> **To play, download the [Otavix Launcher](https://github.com/otavix010/otavix-launcher/releases/latest).** It downloads this port, asks for your `.iso`, makes the game on your PC and keeps it updated. To report a problem or ask for something, use **"Report a problem"** on the game's page in the launcher: the report carries the log and the settings, and that is how fixes come out fastest.

Port do **DiRT 2** (Xbox 360) por **recompilação estática**: o código PowerPC do jogo é traduzido para C++ e compilado como um programa de Windows. Não há emulador de CPU rodando o jogo. A parte gráfica usa o runtime da **Otavix Engine 360**, derivado do ReXGlue e do [Xenia](https://xenia.jp) (veja os Créditos).

**Nada do jogo vem neste repositório.** O port é gerado no seu PC a partir da sua própria cópia (a imagem `.iso` do disco). O código traduzido também é gerado aí e nunca é distribuído.

O runtime é a **Otavix Engine 360 1.0.0** (privada): o gerador baixa o pacote pronto do servidor do launcher e confere o SHA-256. Ela descende do ReXGlue e do Xenia (BSD-3, veja os Créditos) e traz o AMD FidelityFX e as correções do port; os avisos de licença vão no pacote.

O jeito mais fácil de jogar é pelo [Otavix Launcher](https://github.com/otavix010/otavix-launcher), que baixa este port, pede a sua `.iso`, gera tudo e cuida das opções.

![Largada do rallycross em Londres](docs/jogo.jpg)

## O que o port acrescenta

| | Xbox 360 | Port |
|--|--|--|
| Taxa de quadros | 30 fps | **60** ou **120** fps (quadros reais) |
| Resolução interna | 720p | 720p, **1440p** ou 4K |
| Ampliação para a tela | — | AMD FSR 1, AMD CAS, FSR 3 temporal (experimental) ou bilinear, com nitidez ajustável |
| Anti-aliasing | o do jogo | o do jogo, mais FXAA opcional |
| Filtro anisotrópico | o do jogo | até 16x |
| Contador de fps | — | opcional, no canto da tela |

DLSS e XeSS não entram: os dois precisam de vetores de movimento, que os jogos de Xbox 360 não fornecem. O ganho de nitidez vem da resolução interna (supersampling de verdade), e a fluidez vem dos fps reais.

| Londres | Rallycross |
|---|---|
| ![Londres](docs/cena1.jpg) | ![Rallycross](docs/cena2.jpg) |

## Estado dos testes

- Carreira, menus e corrida (Battersea, rallycross) a 60 fps em 2x: média de 60,1 e mínimo de 55 com o carro acelerando, batendo e com dano total.
- 120 fps: o cronômetro da corrida segue o tempo real (5,15 s de corrida em 5,20 s medidos) e a física não muda com a taxa: na mesma arrancada, a velocidade nos mesmos instantes da corrida é a mesma a 60 e a 120 (25 mph a 0,9 s, 58 a 2,6 s, 69 a 3,8 s, 84 a 5,6 s). O motor do jogo (EGO) é o mesmo da versão de PC, que já roda sem trava de quadros. Em 1x a corrida fica entre 100 e 120.
- Brilho certo (com o readback rápido), som em 5.1, replays e flashbacks (unidade de cache).

## Plataformas

| | **Windows** | **Linux / SteamOS** |
|---|---|---|
| Situação | **funciona** (este port) | **não suportado e não testado** |
| Vídeo | Direct3D 12 (o Agility SDK vai ao lado do exe) | o runtime só tem o caminho D3D12 no Windows |
| Como jogar | pelo launcher, ou `gerar.ps1` e `jogar.cmd` | só o port de *God of War: Ascension* tem versão Linux (beta) por enquanto |

## Requisitos

- **Windows 10/11 64 bits** e GPU com **Direct3D 12**.
- **CPU x86-64 com SSE4.1.** AVX não é obrigatório: o gerador compila no seu PC com `-march=native` e usa o que o processador tiver.
- **Visual Studio 2022 Build Tools** com "Desenvolvimento para desktop com C++" e "C++ CMake tools for Windows" (o launcher confere).
- **A sua `.iso`** do *DiRT 2* (DiRT 2).
- **Memória:** o mínimo exato não foi medido. Um cuidado medido: a compilação completa com 16 jobs chegou a ~35 GB de memória comprometida; o gerador limita os jobs (`-Jobs 4` é seguro).
- **Disco:** não medido com precisão: a `.iso`, mais as ferramentas (a engine, ~14 MB, e o Clang portátil) e a pasta de compilação.

## Desempenho medido

FPS de jogo. **Só colocamos o que foi medido**, e com **um jogo só rodando** (com outra carga junto, o desempenho pode cair bastante). Foram medidos no runtime anterior; na engine 1.0.0 a saída da GPU saiu **idêntica quadro a quadro** nos 4 ports e o boot não falhou, mas os FPS **ainda não foram remedidos**.

| Máquina | CPU | GPU | FPS |
|---|---|---|---|
| **PC 1** | Ryzen 7 9800X3D | RTX 5080 | 2x: carreira e corrida (Battersea, rallycross) **média 60,1**, mínimo 55; a 1x a corrida fica entre 100 e 120; 120 validado (mesma física a 60 e a 120) |
| **PC 2** | Core i5-11400F | RX 9060 XT | não medido |
| **Notebook** | Core i5-10300H (4/8) | GTX 1650 | não medido |
| **Portátil** | Legion Go S (Linux) | Radeon 780M | não suportado |

DLSS e XeSS não existem para estes jogos (o Xbox 360 não fornece vetores de movimento); o FSR e o CAS atuam só na saída.

## Problemas conhecidos

- Nenhum problema aberto conhecido hoje.
- Com `readback_resolve=full` em 2x o jogo fica em 52–54; o padrão (`fast`) dá 60.

## Gerar à mão (sem o launcher)

Precisa do **Visual Studio 2022 Build Tools** com "Desenvolvimento para desktop com C++" e "C++ CMake tools for Windows". O gerador baixa o resto: a Otavix Engine 360 e o Clang (LLVM) portátil, numa pasta `_ferramentas` ao lado do port.

```powershell
.\gerar.ps1 -Iso "D:\Jogos\Dirt 2 (USA, Europe).iso"
.\jogar.cmd
```

O port foi feito a partir do **DiRT 2 (USA, Europe)**. O gerador confere o `default.xex` da sua `.iso` (SHA-1 `cdcbe29702fbf18e3e63002096d94d081cbf488f`) e avisa se for outra versão.

## Opções

Ficam em `dirt2.toml` ao lado do executável, ou no arquivo indicado pela variável `PORT_OPCOES`. O launcher grava em `opcoes.toml`. Cada uma também vale na linha de comando (`--fps 120`) ou como variável de ambiente (`REX_FPS=120`).

| Opção | Valores | Padrão |
|--|--|--|
| `fps` | 30, 60, 120 | 60 |
| `resolution_scale` | 1 (720p), 2 (1440p), 3 (4K) | 2 |
| `filtro` | `fsr`, `cas`, `fsr3` (temporal, experimental), `bilinear` | `fsr` |
| `nitidez` | 0 a 100 | 70 |
| `swap_post_effect` | `none`, `fxaa`, `fxaa_extreme` | `none` |
| `anisotropic_override` | -1 (o do jogo), 3 (4x), 4 (8x), 5 (16x) | 5 |
| `fullscreen` | `true`, `false` | `true` |
| `monitor` | 0 (padrão), 1, 2... | 0 |
| `mostrar_fps` | `true`, `false` | `false` |
| `volume` | 0 a 100 | 100 |
| `alvos` | `auto`, `rov`, `rtv`: como a EDRAM é imitada; `auto` usa o caminho medido melhor para o jogo | `auto` |
| `vibration` | `true`, `false` | `true` |
| `zona_morta_esquerda`, `zona_morta_direita` | 0 a 50 (%) | 0 |
| `user_language` | 1 inglês, 3 alemão, 4 francês, 5 espanhol, 6 italiano | 1 |
| `iso` | caminho da `.iso` | — |

## Perguntas frequentes

**Este repositório tem o jogo?** Não. Você precisa da sua cópia (a imagem `.iso` do disco); o gerador monta o port no seu PC.

**Roda no Linux ou no SteamOS?** Ainda não: só o port de *God of War: Ascension* tem versão Linux (beta). Este roda no Windows.

**Saiu atualização. O que acontece com o jogo e os saves?** Atualize pelo launcher: ele refaz a tradução e a compilação uma vez (o gerador guarda a versão do runtime em `out\gerar\sdk.txt`). O jogo e os saves ficam.

**A `.iso` está danificada ou cortada.** O port agora recusa a imagem e diz o motivo no log, em vez de fechar.

**Onde relato um problema?** No launcher, em **"Reportar problema"** na página do jogo.

## Como funciona

- `config/funcoes.toml`: as funções que a análise estática não acha sozinha: chamadas só por ponteiro (nos dados ou com o endereço montado no código) ou fora do alcance da análise. `config/ganchos.toml`: os ganchos no código do jogo. `config/jogo.txt`: a versão do jogo que o gerador confere.
- `src/dirt2_app.h`: a unidade de cache (`cache:`) numa pasta ao lado dos saves, onde o jogo guarda replays e flashbacks: o `XMountUtilityDrive` do jogo é trocado por uma versão que monta a pasta (a ReXGlue responde às partições de cache com um dispositivo nulo, e a montagem original desistia).
- `config/ganchos.toml`: o intervalo de apresentação de 2 vblanks (30 fps) vira 1 a 60 fps; o cronômetro das corridas segue o tempo real.
- O brilho: o jogo mede a exposição lendo pela CPU a imagem que acabou de desenhar. Sem essa leitura, que o runtime deixa desligada por padrão, todas as cenas e menus saíam escuros. O port liga a leitura do quadro anterior (`readback_resolve = fast`, como as notas de compatibilidade do Xenia indicam), que dá o brilho certo a 60 fps.
- `src/port/`: a base comum dos ports de Xbox 360 (a mesma em todos): opções de imagem, contador de fps, leitura da `.iso`, a trava que corrige uma corrida na entrada de controles do runtime, `falha.log` com a pilha em caso de falha.

Para desenvolver: `build.cmd` compila; `scripts/rodar.py` roda numa janela com prints, o fps de cada segundo e um controle roteirizado (`PORT_PAD`; para começar um jogo novo: `--pad 12:START,20:START,25-150@3:A`); `scripts/tecla.py` aperta botões no jogo em execução; `scripts/varrer_ponteiros.py` e `scripts/desmontar.py` ajudam a achar funções.

## Créditos

- [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk): recompilador estático e runtime de Xbox 360 (BSD-3).
- [Xenia](https://github.com/xenia-project/xenia): o emulador em que o runtime se baseia (BSD-3).

DiRT 2 é marca da Codemasters. Este projeto não tem relação com ela nem com a Microsoft.

## Licença

O código deste repositório está sob a licença MIT (`LICENSE`). O SDK e o runtime têm a licença própria deles (BSD-3).
