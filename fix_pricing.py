content = open('index.html', encoding='utf-8').read()

old_pricing = '''<!-- PRICING -->
<section id="pricing">
  <div class="container">
    <div class="eyebrow reveal">Pricing</div>
    <h2 class="section-title reveal">Simple, transparent pricing.<br>No per-seat nonsense.</h2>
    <p class="section-sub reveal">First 3-5 customers get 60-day free trials as design partners. Subsequent customers get 14-day trials.</p>
    <div class="pricing-grid">
      <div class="pricing-card reveal">
        <div class="pricing-name">Supervised</div>
        <div class="pricing-desc">AI recommends, analysts decide. Perfect for teams getting started with autonomous security.</div>
        <div class="pricing-price">$500<span>/mo</span></div>
        <div class="pricing-period">Unlimited users · Up to 10k events/day</div>
        <div class="pricing-features">
          <div class="pricing-feature">Full detection pipeline</div>
          <div class="pricing-feature">MITRE ATT&amp;CK mapping</div>
          <div class="pricing-feature">26 SOAR actions (approval mode)</div>
          <div class="pricing-feature">Weekly CISO PDF report</div>
          <div class="pricing-feature">Webhook integrations</div>
          <div class="pricing-feature">14-day free trial</div>
        </div>
        <a href="https://app.domesoc.com/signup" class="pricing-cta pricing-cta-ghost">Start free trial</a>
      </div>
      <div class="pricing-card featured reveal" style="transition-delay:0.1s">
        <div class="pricing-badge">MOST POPULAR</div>
        <div class="pricing-name">Autonomous</div>
        <div class="pricing-desc">AI acts within your confidence thresholds. The sweet spot for most security teams.</div>
        <div class="pricing-price">$2,500<span>/mo</span></div>
        <div class="pricing-period">Unlimited users · Unlimited events</div>
        <div class="pricing-features">
          <div class="pricing-feature">Everything in Supervised</div>
          <div class="pricing-feature">Autonomous containment mode</div>
          <div class="pricing-feature">12 native integrations</div>
          <div class="pricing-feature">VirusTotal IP enrichment</div>
          <div class="pricing-feature">Detection tuning &amp; whitelisting</div>
          <div class="pricing-feature">SLA tracking &amp; compliance</div>
          <div class="pricing-feature">14-day free trial</div>
        </div>
        <a href="https://app.domesoc.com/signup" class="pricing-cta pricing-cta-primary">Start free trial</a>
      </div>
      <div class="pricing-card reveal" style="transition-delay:0.2s">
        <div class="pricing-name">Full Autonomous</div>
        <div class="pricing-desc">Zero human intervention. For mature security teams that trust the AI completely.</div>
        <div class="pricing-price">$15,000<span>/mo</span></div>
        <div class="pricing-period">Unlimited seats · All features unlocked</div>
        <div class="pricing-features">
          <div class="pricing-feature">Everything in Autonomous</div>
          <div class="pricing-feature">Full autonomous mode</div>
          <div class="pricing-feature">Legal acknowledgment workflow</div>
          <div class="pricing-feature">Endpoint agent deployment</div>
          <div class="pricing-feature">Dedicated onboarding</div>
          <div class="pricing-feature">SLA guarantee</div>
          <div class="pricing-feature">60-day design partner trial</div>
        </div>
        <a href="https://app.domesoc.com/signup" class="pricing-cta pricing-cta-ghost">Get started</a>
      </div>
    </div>
  </div>
</section>'''

new_pricing = '''<!-- PRICING -->
<section id="pricing">
  <div class="container">
    <div class="eyebrow reveal">Pricing</div>
    <h2 class="section-title reveal">Replace your tier-1 analyst.<br>Not your budget.</h2>
    <p class="section-sub reveal">One tier-1 SOC analyst costs $75,000+/yr. DomeSOC Autonomous starts at $2,500/mo — and never sleeps, never misses, never calls in sick.</p>

    <div style="background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.15);border-radius:12px;padding:20px 28px;margin-bottom:40px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;" class="reveal">
      <div style="font-size:14px;color:var(--lgray);">💡 <strong style="color:var(--white)">Design partner program:</strong> First 3–5 customers get 60-day free trials and direct input into the product roadmap.</div>
      <a href="mailto:hello@domesoc.com" style="font-size:13px;color:var(--blue);text-decoration:none;white-space:nowrap;">Apply as design partner →</a>
    </div>

    <div class="pricing-grid">
      <div class="pricing-card reveal">
        <div class="pricing-name">Supervised</div>
        <div class="pricing-desc">AI brain, human hands. Full detection and analysis — your team approves every action.</div>
        <div class="pricing-price">$1,000<span>/mo</span></div>
        <div class="pricing-period">Unlimited users · Up to 10k events/day</div>
        <div style="background:rgba(255,255,255,0.03);border-radius:8px;padding:14px;margin:16px 0;font-size:12px;color:var(--gray);line-height:1.6;">
          Best for teams that want AI-powered detection and analysis but prefer to keep humans in control of every response action.
        </div>
        <div class="pricing-features">
          <div class="pricing-feature">Full 3-network AI detection pipeline</div>
          <div class="pricing-feature">Claude threat assessment on every detection</div>
          <div class="pricing-feature">MITRE ATT&amp;CK mapping &amp; confidence scoring</div>
          <div class="pricing-feature">All 26 SOAR actions — analyst approval required</div>
          <div class="pricing-feature">Webhook integrations for custom SOAR</div>
          <div class="pricing-feature">Weekly CISO PDF report</div>
          <div class="pricing-feature">Full audit trail &amp; decision reasoning</div>
          <div class="pricing-feature">14-day free trial — no credit card</div>
        </div>
        <a href="https://app.domesoc.com/signup" class="pricing-cta pricing-cta-ghost">Start free trial</a>
      </div>

      <div class="pricing-card featured reveal" style="transition-delay:0.1s">
        <div class="pricing-badge">REPLACES TIER-1 ANALYST</div>
        <div class="pricing-name">Autonomous</div>
        <div class="pricing-desc">AI brain, AI hands. Threats contained automatically within your confidence thresholds.</div>
        <div class="pricing-price">$2,500<span>/mo</span></div>
        <div class="pricing-period">Unlimited users · Unlimited events/day</div>
        <div style="background:rgba(59,130,246,0.08);border-radius:8px;padding:14px;margin:16px 0;font-size:12px;color:var(--lgray);line-height:1.6;">
          Best for security teams ready to let AI handle containment. You set the confidence threshold — everything above it gets contained automatically.
        </div>
        <div class="pricing-features">
          <div class="pricing-feature">Everything in Supervised</div>
          <div class="pricing-feature">Autonomous containment — no analyst needed</div>
          <div class="pricing-feature">Per-action permissions — granular control</div>
          <div class="pricing-feature">12 native integrations — CrowdStrike, Okta, Jira &amp; more</div>
          <div class="pricing-feature">VirusTotal IP enrichment on every detection</div>
          <div class="pricing-feature">Detection tuning — whitelist &amp; suppress rules</div>
          <div class="pricing-feature">SLA tracking &amp; compliance dashboard</div>
          <div class="pricing-feature">14-day free trial — no credit card</div>
        </div>
        <a href="https://app.domesoc.com/signup" class="pricing-cta pricing-cta-primary">Start free trial</a>
      </div>

      <div class="pricing-card reveal" style="transition-delay:0.2s">
        <div class="pricing-name">Full Autonomous</div>
        <div class="pricing-desc">Zero human intervention. The AI handles everything — detection, decision, containment.</div>
        <div class="pricing-price">$15,000<span>/mo</span></div>
        <div class="pricing-period">Unlimited seats · All features unlocked</div>
        <div style="background:rgba(255,255,255,0.03);border-radius:8px;padding:14px;margin:16px 0;font-size:12px;color:var(--gray);line-height:1.6;">
          Best for mature security teams running 24/7 operations without analyst on-call. Requires legal acknowledgment before activation.
        </div>
        <div class="pricing-features">
          <div class="pricing-feature">Everything in Autonomous</div>
          <div class="pricing-feature">Full autonomous mode — zero human required</div>
          <div class="pricing-feature">Legal acknowledgment &amp; liability workflow</div>
          <div class="pricing-feature">Endpoint agent deployment</div>
          <div class="pricing-feature">Dedicated onboarding &amp; configuration</div>
          <div class="pricing-feature">SLA guarantee with response commitment</div>
          <div class="pricing-feature">Quarterly security reviews</div>
          <div class="pricing-feature">60-day design partner trial</div>
        </div>
        <a href="https://app.domesoc.com/signup" class="pricing-cta pricing-cta-ghost">Get started</a>
      </div>
    </div>

    <div style="margin-top:32px;padding:20px 28px;border:1px solid var(--border);border-radius:12px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;text-align:center;" class="reveal">
      <div>
        <div style="font-size:13px;font-weight:600;color:var(--white);margin-bottom:4px;">No per-seat pricing</div>
        <div style="font-size:12px;color:var(--gray);">Add your whole team. One flat monthly rate regardless of headcount.</div>
      </div>
      <div>
        <div style="font-size:13px;font-weight:600;color:var(--white);margin-bottom:4px;">Cancel anytime</div>
        <div style="font-size:12px;color:var(--gray);">No annual lock-in. No setup fees. No professional services required.</div>
      </div>
      <div>
        <div style="font-size:13px;font-weight:600;color:var(--white);margin-bottom:4px;">Start in minutes</div>
        <div style="font-size:12px;color:var(--gray);">Send your first detection via webhook and see AI analysis within seconds.</div>
      </div>
    </div>
  </div>
</section>'''

if old_pricing in content:
    content = content.replace(old_pricing, new_pricing, 1)
    print('OK')
else:
    print('FAIL')
    idx = content.find('<!-- PRICING -->')
    print('pricing at:', idx)

open('index.html', 'w', encoding='utf-8', newline='\n').write(content)
print('Done')
