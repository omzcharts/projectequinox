/* Project Equinox — Remake: tiny, dependency-free behaviours */
(function(){
  /* mobile menu */
  var btn=document.querySelector('.menu-btn'), links=document.querySelector('.nav-links');
  if(btn&&links){
    btn.addEventListener('click',function(){
      var open=links.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
      btn.textContent=open?'Close':'Menu';
    });
  }

  /* tabs (media page) — deep-linkable via #podcasts, #videos, #articles, #press */
  var tabs=document.querySelectorAll('[role="tab"]');
  if(tabs.length){
    var show=function(id){
      tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.panel===id?'true':'false');});
      document.querySelectorAll('.panel').forEach(function(p){p.hidden=(p.id!==id);});
    };
    tabs.forEach(function(t){t.addEventListener('click',function(){
      show(t.dataset.panel); history.replaceState(null,'','#'+t.dataset.panel);
    });});
    var h=location.hash.replace('#','');
    if(h&&document.getElementById(h)&&document.getElementById(h).classList.contains('panel')) show(h);
  }

  /* generic filter chips (articles by topic, stories by type) */
  document.querySelectorAll('[data-filter-group]').forEach(function(group){
    var target=document.querySelector(group.dataset.filterGroup);
    if(!target) return;
    group.querySelectorAll('.chip').forEach(function(chip){
      chip.addEventListener('click',function(){
        group.querySelectorAll('.chip').forEach(function(c){c.setAttribute('aria-pressed',c===chip?'true':'false');});
        var f=chip.dataset.filter;
        target.querySelectorAll('[data-topic]').forEach(function(item){
          item.hidden=!(f==='all'||item.dataset.topic.split(' ').indexOf(f)>-1);
        });
      });
    });
  });

  /* read-more on long stories */
  document.querySelectorAll('.story .more').forEach(function(b){
    b.addEventListener('click',function(){
      var body=b.parentElement.querySelector('.body');
      var collapsed=body.classList.toggle('clamp');
      b.textContent=collapsed?'Read the full story':'Show less';
      b.setAttribute('aria-expanded',collapsed?'false':'true');
    });
  });

  /* optional pre-call note -> opens the visitor's email app, pre-filled */
  var form=document.getElementById('prep-form');
  if(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var d=new FormData(form);
      var body='Hi Andre,\n\n'+
        'Name: '+(d.get('name')||'')+'\n'+
        'I am: '+(d.get('who')||'')+'\n'+
        'Relationship status: '+(d.get('status')||'')+'\n\n'+
        'What I would most like help with:\n'+(d.get('goal')||'')+'\n\n'+
        'Preferred timing to start: '+(d.get('when')||'')+'\n';
      location.href='mailto:andrecoaching1@gmail.com?subject='+encodeURIComponent('Complimentary call request')+'&body='+encodeURIComponent(body);
    });
  }
})();
