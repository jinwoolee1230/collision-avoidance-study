
# SAC load and play (tf2 subclassing API version)
# coded by St.Watermelon
## 학습된 신경망 파라미터를 가져와서 에이전트를 실행시키는 파일

# 필요한 패키지 임포트
from train import SACagent
import tensorflow as tf
from envs.jinwoo_env import AirSimDroneEnv

def main():

    env = AirSimDroneEnv('127.0.0.1') 
    agent = SACagent(env)  # SAC 에이전트 객체
    

    # print(state['depth'].shape, state['dynamic_state'].shape)

    # 행동 샘플링
    state = env.reset() 
    action = agent.actor(state['depth'], state['dyn_state'], state["position"], state["global_pos"])
    print(action)
    agent.load_weights('/home/mw/collision-avoidance-study/collision_avoid_SAC/save_weights/')  # 신경망 파라미터 가져옴
    
    for _ in range(100000000):
        time = 0
        state = env.reset()  # 환경을 초기화하고, 초기 상태 관측
        while True:
            env.render()
            # 행동 계산
            action = agent.get_action(state['depth'], state['dyn_state'], state["position"], state["global_pos"])

            state, reward, done, _ = env.step(action)
            time += 1

            print('Time: ', time, 'Reward: ', reward)

            if done:
                break

    env.close()


if __name__=="__main__":
    main()