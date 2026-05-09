/**
 * Canvas helpers for textbook-style parallel conductor diagrams (magnetism).
 * Vertical wires, current arrows, dimensions, and marked field points.
 */
(function (global) {
  "use strict";

  const defaults = {
    wireColor: "#e8eaf0",
    dimColor: "#9aa3b8",
    pointColor: "#6c8cff",
    labelFont: '14px "Segoe UI", Roboto, sans-serif',
    mathFont: '15px "Times New Roman", Times, serif',
    bg: "#0f1117",
  };

  function setupHiDPICanvas(canvas, cssW, cssH) {
    const dpr = Math.min(global.devicePixelRatio || 1, 2);
    canvas.style.width = cssW + "px";
    canvas.style.height = cssH + "px";
    canvas.width = Math.round(cssW * dpr);
    canvas.height = Math.round(cssH * dpr);
    const ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx, cssW, cssH, dpr };
  }

  function drawLine(ctx, x1, y1, x2, y2, opts) {
    const o = Object.assign({ width: 2, color: defaults.wireColor }, opts);
    ctx.save();
    ctx.strokeStyle = o.color;
    ctx.lineWidth = o.width;
    ctx.lineCap = "round";
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.restore();
  }

  /**
   * Arrow along vertical segment; dir 1 = toward increasing y (down on canvas).
   */
  function drawCurrentArrowVertical(ctx, x, y0, y1, dir, opts) {
    const o = Object.assign(
      { color: defaults.wireColor, headLen: 10, headWidth: 7, at: 0.52 },
      opts
    );
    const yLo = Math.min(y0, y1);
    const yHi = Math.max(y0, y1);
    const ya = yLo + (yHi - yLo) * o.at;
    const tipY = dir >= 0 ? ya + o.headLen * 0.6 : ya - o.headLen * 0.6;
    const baseY = dir >= 0 ? ya - o.headLen * 0.5 : ya + o.headLen * 0.5;
    ctx.save();
    ctx.fillStyle = o.color;
    ctx.beginPath();
    ctx.moveTo(x, tipY);
    ctx.lineTo(x - o.headWidth / 2, baseY);
    ctx.lineTo(x + o.headWidth / 2, baseY);
    ctx.closePath();
    ctx.fill();
    ctx.restore();
  }

  function drawWireVertical(ctx, x, yTop, yBot, currentLabel, dirY, style) {
    const st = Object.assign({}, defaults, style);
    drawLine(ctx, x, yTop, x, yBot, { color: st.wireColor, width: 2.5 });
    drawCurrentArrowVertical(ctx, x, yTop, yBot, dirY, { color: st.wireColor });
    if (currentLabel) {
      ctx.save();
      ctx.font = st.mathFont;
      ctx.fillStyle = st.wireColor;
      ctx.textAlign = "center";
      ctx.textBaseline = "bottom";
      ctx.fillText(currentLabel, x, yTop - 6);
      ctx.restore();
    }
  }

  /**
   * Horizontal dimension between x1 and x2 at y; label centered below.
   */
  function drawHorizontalDimension(ctx, x1, x2, y, label, style) {
    const st = Object.assign({}, defaults, style);
    const left = Math.min(x1, x2);
    const right = Math.max(x1, x2);
    const tick = 7;
    ctx.save();
    ctx.strokeStyle = st.dimColor;
    ctx.fillStyle = st.dimColor;
    ctx.lineWidth = 1;
    // ticks
    ctx.beginPath();
    ctx.moveTo(left, y - tick);
    ctx.lineTo(left, y + tick);
    ctx.moveTo(right, y - tick);
    ctx.lineTo(right, y + tick);
    ctx.stroke();
    // dimension line
    drawLine(ctx, left, y, right, y, { width: 1, color: st.dimColor });
    // end arrows (inward)
    const ah = 6;
    const aw = 4;
    ctx.beginPath();
    ctx.moveTo(left + ah, y - aw);
    ctx.lineTo(left, y);
    ctx.lineTo(left + ah, y + aw);
    ctx.moveTo(right - ah, y - aw);
    ctx.lineTo(right, y);
    ctx.lineTo(right - ah, y + aw);
    ctx.stroke();
    if (label) {
      ctx.font = st.mathFont;
      ctx.textAlign = "center";
      ctx.textBaseline = "top";
      ctx.fillText(label, (left + right) / 2, y + 10);
    }
    ctx.restore();
  }

  function drawMarkedPoint(ctx, x, y, label, style) {
    const st = Object.assign({}, defaults, style);
    const r = 5;
    ctx.save();
    ctx.strokeStyle = st.pointColor;
    ctx.fillStyle = "transparent";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.stroke();
    ctx.font = st.labelFont;
    ctx.fillStyle = st.pointColor;
    ctx.textAlign = "left";
    ctx.textBaseline = "bottom";
    ctx.fillText(label, x + 8, y - 8);
    ctx.restore();
  }

  function clearScene(ctx, w, h, bg) {
    ctx.save();
    ctx.fillStyle = bg || defaults.bg;
    ctx.fillRect(0, 0, w, h);
    ctx.restore();
  }

  /**
   * @param {HTMLCanvasElement} canvas
   * @param {object} scene
   * @param {Array<{x:number,label:string,dirY:number}>} scene.wires — dirY: +1 current downward
   * @param {number} scene.yTop
   * @param {number} scene.yBot
   * @param {Array<{x1:number,x2:number,y:number,label:string}>} [scene.dimensions]
   * @param {Array<{x:number,y:number,label:string}>} [scene.points]
   */
  function renderParallelWires(canvas, scene, style) {
    const cssW = scene.width || 560;
    const cssH = scene.height || 360;
    const { ctx, cssW: W, cssH: H } = setupHiDPICanvas(canvas, cssW, cssH);
    const st = Object.assign({}, defaults, style);
    clearScene(ctx, W, H, st.bg);

    const yTop = scene.yTop ?? 56;
    const yBot = scene.yBot ?? H - 72;

    (scene.wires || []).forEach(function (w) {
      drawWireVertical(ctx, w.x, yTop, yBot, w.label, w.dirY == null ? 1 : w.dirY, st);
    });

    (scene.dimensions || []).forEach(function (d) {
      drawHorizontalDimension(ctx, d.x1, d.x2, d.y, d.label, st);
    });

    (scene.points || []).forEach(function (p) {
      drawMarkedPoint(ctx, p.x, p.y, p.label, st);
    });

    return { ctx, width: W, height: H };
  }

  global.EMParallelWiresCanvas = {
    setupHiDPICanvas,
    renderParallelWires,
    defaults,
  };
})(typeof window !== "undefined" ? window : globalThis);
